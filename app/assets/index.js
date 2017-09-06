(function() {

  Promise.prototype.progress = function(onprogress) {
    this.onprogress = onprogress;
    return this;
  };

  var http = {
    request: function(url, options) {
      options = options || {};
      var id = [Date.now(), Math.floor(Math.random() * 100)].join('.');
      let xhr = new XMLHttpRequest();
      const p = new Promise((resolve, reject) => {
        xhr.onreadystatechange = () => {
          if (xhr.readyState != XMLHttpRequest.DONE) return;
          if (xhr.status >= 400) {
            return reject({id: id, status: xhr.status, message: xhr.response || xhr.statusText});
          }
          resolve({id: id, data: xhr.response});
        };
        xhr.upload.onprogress = (ev) => {
          if (typeof this.onprogress != 'function') return;
          this.onprogress({id:id, loaded:ev.loaded, total: ev.total});
        };
      });
      xhr.open(options.method, url, true);
      xhr.withCredentials = true;
      if (options.responseType) xhr.responseType = options.responseType;
      (options.body) ? xhr.send(options.body) : xhr.send();
      return p;
    },
    post: function(url, data, type) {
      data = data || {};
      return this.request(url, {method:'POST', body:data, responseType: type});
    },
  }

  var OCRController = function(root) {
    this.root = root;
    this.input = this.root.querySelector('input[type=file]');
    this.button = this.root.querySelector('button');
    this.button.addEventListener('click', this.submit.bind(this));
    this.output = this.root.querySelector('code');
  };
  OCRController.prototype.submit = function() {
    if (this.input.files.length == 0) return alert('No image file specified');
    var self = this;
    var data = new FormData();
    data.append("file", this.input.files[0]);
    data.append("trim", "\n");
    http.post("/file", data).progress(function(progress) {
      console.log('progress', progress);
    }).then(function(res) {
      self.output.innerHTML = res.data;
    }).catch(function(err) {
      self.output.innerHTML = err.message;
    });
  };

  var AVConvController = function(root) {
    this.root = root;
    this.input = this.root.querySelector('input[type=file]');
    this.button = this.root.querySelector('button');
    this.button.addEventListener('click', this.submit.bind(this));
    this.output = this.root.querySelector('code');
  };
  AVConvController.prototype.submit = function() {
    if (this.input.files.length == 0) return alert('No image file specified');
    var self = this;
    var data = new FormData();
    data.append("file", this.input.files[0]);
    http.post("/video/convert", data, 'blob').progress(function(progress) {
      console.log('progress', progress);
    }).then(function(res) {
      var url = URL.createObjectURL(res.data);
      var a = document.createElement('a');
      a.download = 'result.mp4';
      a.href= url;
      document.body.appendChild(a);
      a.click();
      a.remove();
    }).catch(function(err) {
      self.output.innerHTML = err.message || err.status;
    });
  }

  this.ocr    = new OCRController(document.querySelector("section#form-ocr"));
  this.avconv = new AVConvController(document.querySelector("section#form-avconv"));
})();
