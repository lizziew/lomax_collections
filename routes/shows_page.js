var express = require('express');
var router = express.Router();

router.get('/shows_page', function(req, res) {
	res.render('shows_page', {title: 'shows'});
});

module.exports = router;
