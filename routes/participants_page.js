var express = require('express');
var router = express.Router();

router.get('/participants_page', function(req, res) {
	res.render('participants_page', {title: 'participants'});
});

module.exports = router;
