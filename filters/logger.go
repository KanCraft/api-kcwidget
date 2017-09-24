package filters

import (
	"log"
	"net/http"
)

// LogFilter output access log.
type LogFilter struct {
	logger *log.Logger
	Next   http.Handler
}

// NewLogFilter constructs LogFilter.
func NewLogFilter(logger *log.Logger) *LogFilter {
	return &LogFilter{
		logger: logger,
	}
}

// SetNext for marmoset.Filter
func (f *LogFilter) SetNext(next http.Handler) {
	f.Next = next
}

func (f *LogFilter) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	f.logger.Println(r.Method, r.URL.Path)
	f.Next.ServeHTTP(w, r)
}
