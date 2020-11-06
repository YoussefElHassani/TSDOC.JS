(function (sandbox) {
    function MyAnalysis() {

        /**
         * This callback is called when the execution of a function body completes
         *
         * @param {number} iid - Static unique instruction identifier of this callback
         * @param {*} returnVal - The value returned by the function
         * @param {{exception:*} | undefined} wrappedExceptionVal - If this parameter is an object, the function
         * execution has thrown an uncaught exception and the exception is being stored in the <tt>exception</tt>
         * property of the parameter
         * @returns {{returnVal: *, wrappedExceptionVal: *, isBacktrack: boolean}}  If an object is returned, then the
         * actual <tt>returnVal</tt> and <tt>wrappedExceptionVal.exception</tt> are replaced with that from the
         * returned object. If an object is returned and the property <tt>isBacktrack</tt> is set, then the control-flow
         * returns to the beginning of the function body instead of returning to the caller.  The property
         * <tt>isBacktrack</tt> can be set to <tt>true</tt> to repeatedly execute the function body as in MultiSE
         * symbolic execution.
         */
        this.functionExit = function (iid, returnVal, wrappedExceptionVal) {
            console.log("functionExit")
            var shadowObj = sandbox.smemory.getShadowFrame(returnVal);
            console.log("FUNCTION EXIT "+sandbox.smemory.getIDFromShadowObjectOrFrame(shadowObj)+"." + returnVal +" at " + J$.iidToLocation(J$.sid, iid));
            console.log({returnVal: returnVal, wrappedExceptionVal: wrappedExceptionVal, isBacktrack: false});
            return {returnVal: returnVal, wrappedExceptionVal: wrappedExceptionVal, isBacktrack: false};
        };

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
            console.log("ScriptExit")
            console.log({wrappedExceptionVal: wrappedExceptionVal, isBacktrack: false, location: J$.iidToLocation(J$.sid, iid)});
            return {wrappedExceptionVal: wrappedExceptionVal, isBacktrack: false};
        };

    }

    sandbox.analysis = new MyAnalysis();
})(J$);