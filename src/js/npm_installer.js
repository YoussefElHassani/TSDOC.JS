var fs = require('fs');
var npm = require('npm');

const files = fs.readdirSync('../dts-generate-results/results/4_extract-code/code/');

npm.load(function(err) {
    // handle errors
    
    // install module ffi
    npm.commands.install(files, function(er, data) {
        // log errors or data
    });
    
    npm.on('log', function(message) {
        // log installation progress
        console.log(message);
    });
});
