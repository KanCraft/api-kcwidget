package main

import (
	"log"
	"net/http"
	"os"
	"runtime"
	"time"

	"github.com/otiai10/marmoset"

	ocrserver "github.com/otiai10/ocrserver/controllers"
	webm2mp4 "github.com/otiai10/webm2mp4/controllers"
)

const version = "0.3.0"

func main() {

	logger := log.New(os.Stdout, "", log.Ltime)

	marmoset.LoadViews("./app/views")

	r := marmoset.NewRouter()

	// API
	r.GET("/status", status)
	r.POST("/base64", ocrserver.Base64)
	r.POST("/file", ocrserver.FileUpload)
	r.POST("/video/convert", webm2mp4.Convert)

	// Pages (You ain't gonna need it)
	r.Static("/assets", "./app/assets")
	r.GET("/", index)

	if os.Getenv("LOG_ENABLED") != "" {
		r.Apply(NewLogFilter(logger))
	}

	port := os.Getenv("PORT")
	logger.Printf("listening on port %s", port)
	err := http.ListenAndServe(":"+port, r)
	logger.Println(err)
}

func status(w http.ResponseWriter, r *http.Request) {
	render := marmoset.Render(w, true)
	render.JSON(http.StatusOK, marmoset.P{"message": "OK!", "version": version})
}

func index(w http.ResponseWriter, r *http.Request) {
	render := marmoset.Render(w)

	var m runtime.MemStats
	runtime.ReadMemStats(&m)
	render.HTML("index", marmoset.P{
		"version":   version,
		"memory":    m,
		"timestamp": time.Now().Unix(),
	})
}
