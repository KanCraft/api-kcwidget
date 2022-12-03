package main

import (
	"log"
	"net/http"
	"os"
	"runtime"
	"time"

	"github.com/otiai10/marmoset"

	ocrserver "github.com/otiai10/ocrserver/controllers"
)

const version = "0.4.1"

func main() {

	logger := log.New(os.Stdout, "", log.Ltime)

	marmoset.LoadViews("./app/views")

	r := marmoset.NewRouter()

	// General
	r.GET("/status", status)
	// OCR
	r.POST("/ocr/base64", ocrserver.Base64)
	r.POST("/ocr/file", ocrserver.FileUpload)

	// WebM to MP4
	// r.POST("/video/convert", webm2mp4.Convert)

	// Pages (You ain't gonna need it)
	r.Static("/assets", "./app/assets")
	r.GET("/", index)

	// if os.Getenv("LOG_ENABLED") != "" {
	// 	r.Apply(filters.NewLogFilter(logger))
	// }

	port := os.Getenv("PORT")
	if port == "" {
		panic("PORT must be specified.")
	}
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
