package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os"

	"github.com/otiai10/marmoset"

	"github.com/otiai10/ocrserver/config"
	"github.com/otiai10/ocrserver/controllers"
)

var logger *log.Logger

const version = "0.2.0"

func main() {

	logger = log.New(os.Stdout, fmt.Sprintf("[%s] ", config.AppName()), 0)

	r := marmoset.NewRouter()

	// API
	r.GET("/status", func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusOK)
		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(map[string]interface{}{
			"message": "OK!",
			"version": version,
		})
	})
	r.POST("/base64", controllers.Base64)
	r.POST("/file", controllers.FileUpload)

	// Pages (You ain't gonna need it)
	// r.Static("/assets", "./assets")
	// r.GET("/", Index)

	logger.Printf("listening on port %s", config.Port())
	err := http.ListenAndServe(config.Port(), r)
	logger.Println(err)
}
