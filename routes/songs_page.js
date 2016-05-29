var express = require('express');
var router = express.Router();

router.get('/songs_page', function(req, res) {
	res.render('songs_page', {title: 'songs'});
});

module.exports = router;
