// Importing Libraries
const log4js = require("log4js");
const {serializeError, deserializeError} = require('serialize-error');

// adding layout
log4js.addLayout('json', function(config) {
    return function(logEvent) { return JSON.stringify(logEvent) + config.separator; }
  });
// Configuring Logger
log4js.configure({
  appenders: {  infoLogger:{ type: "fileSync", layout: { type: 'json', separator: ',' } ,filename: "./log/info.log"}},
  categories: { default: { appenders: ["infoLogger"], level: "info" } }
});
// Calling Logger
const infoLogger = log4js.getLogger("infoLogger'");




(function (sandbox) {
    function MyAnalysis() {

        /**
         * This callback is called when the execution of a JavaScript file completes
         *
         * @param {number} iid - Static unique instruction identifier of this callback
         * @param {{exception:*} | undefined} wrappedExceptionVal - If this parameter is an object, the script
         * execution has thrown an uncaught exception and the exception is being stored in the <tt>exception</tt>
         * property of the parameter
         * @returns {{wrappedExceptionVal: *, isBacktrack: boolean}} - If an object is returned, then the
         * actual <tt>wrappedExceptionVal.exception</tt> is replaced with that from the
         * returned object. If an object is returned and the property <tt>isBacktrack</tt> is set, then the control-flow
         * returns to the beginning of the script body.  The property
         * <tt>isBacktrack</tt> can be set to <tt>true</tt> to repeatedly execute the script body as in MultiSE
         * symbolic execution.
          */
        this.scriptExit = function (iid, wrappedExceptionVal) {
            // Get the location of the file being analysis
            location = J$.iidToLocation(J$.sid, iid);
            // Get the path from the location
            filename = location.split(':')[0];
            filename = filename.replace("(","");
            // Log filename and the captured exception 
            if(wrappedExceptionVal === undefined) {
                    if(!filename.includes("node_modules")){
                    infoLogger.info({'file': filename, 'wrappedExceptionVal': null, 'flag': "Success"})
                    log4js.shutdown(() => {});
                }
            } else{
                if(!filename.includes("node_modules")){
                    error = serializeError(wrappedExceptionVal)
                    infoLogger.info({'file': filename, 'wrappedExceptionVal': JSON.stringify(error), 'flag': "Error"})
                    log4js.shutdown(() => {});
                }
            }

        }; 

    }
    sandbox.analysis = new MyAnalysis();
})(J$);