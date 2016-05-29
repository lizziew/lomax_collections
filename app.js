var express = require('express');
var path = require('path');
var favicon = require('serve-favicon');
var logger = require('morgan');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');

var routes = require('./routes/index');
var songs_page = require('./routes/songs_page');
var shows_page = require('./routes/shows_page');
var participants_page = require('./routes/participants_page');

var mysql = require('mysql');
var fs = require('fs');

var app = express();

// view engine setup
app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');

app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(__dirname + '/public'));

app.use('/', routes);
app.use('/songs_page', songs_page);
app.use('/shows_page', shows_page);
app.use('/participants_page', participants_page);

app.get('/index', function(request, response) {
  response.render('index');
});

app.get('/songs_page', function(request, response) {
  response.render('songs_page'); 
});

app.get('/shows_page',  function(request, response) {
  response.render('shows_page'); 
});

app.get('/participants_page',  function(request, response) {
  response.render('participants_page'); 
});

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  var err = new Error('Not Found');
  err.status = 404;
  next(err);
});

//***
// var connection = mysql.createConnection({
//    host: 'localhost',
//    user: 'root',
//    password: '54321'
// });

// connection.connect();

// var query = 'select * from lomax_radio.tracksong;';

// connection.query(query, function(err, results, fields) {
//     if(err) throw err;

//     fs.writeFile('table.json', JSON.stringify(results), function (err) {
//       if (err) throw err;
//       console.log('Saved!');
//     });

//     connection.end();
// });

// error handlers

// development error handler
// will print stacktrace
if (app.get('env') === 'development') {
  app.use(function(err, req, res, next) {
    res.status(err.status || 500);
    res.render('error', {
      message: err.message,
      error: err
    });
  });
}

// production error handler
// no stacktraces leaked to user
app.use(function(err, req, res, next) {
  res.status(err.status || 500);
  res.render('error', {
    message: err.message,
    error: {}
  });
});


module.exports = app;
