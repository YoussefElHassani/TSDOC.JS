import os

# Successfully parced files
target = ''
target_dir = ''

node = "node ../jalangi2/src/js/commands/jalangi.js --inlineSource --inlineIID --analysis ../run-time-information-gathering/utils/initialize.js --analysis ../run-time-information-gathering/utils/sMemory/sMemory.js --analysis ../run-time-information-gathering/utils/functions.js --analysis ../run-time-information-gathering/utils/functionsExecutionStack.js --analysis ../run-time-information-gathering/utils/sMemoryInterface.js --analysis ../run-time-information-gathering/utils/objectSerializer.js --analysis ../run-time-information-gathering/utils/interactionSerializer.js --analysis ../run-time-information-gathering/utils/interactionContainerFinder.js --analysis ../run-time-information-gathering/utils/objectTraceIdMap.js --analysis ../run-time-information-gathering/utils/recursiveInteractionsHandler.js --analysis ../run-time-information-gathering/utils/argumentWrapperObjectBuilder.js --analysis ../run-time-information-gathering/utils/functionIdHandler.js --analysis ../run-time-information-gathering/utils/argumentProxyBuilder.js --analysis ../run-time-information-gathering/utils/interactionWithResultHandler.js --analysis ../run-time-information-gathering/utils/wrapperObjectsHandler.js --analysis ../run-time-information-gathering/utils/toPrimitive.js --analysis ../run-time-information-gathering/utils/operators/relationalComparisonOperatorTypeCoercion.js --analysis ../run-time-information-gathering/utils/operators/sumOperatorTypeCoercion.js --analysis ../run-time-information-gathering/utils/operators/operatorsTypeCoercionAnalyzer.js --analysis ../run-time-information-gathering/utils/argumentContainer.js --analysis ../run-time-information-gathering/utils/functionContainer.js --analysis ../run-time-information-gathering/utils/interactions/interaction.js --analysis ../run-time-information-gathering/utils/interactions/activeInteraction.js --analysis ../run-time-information-gathering/utils/interactions/getFieldInteraction.js --analysis ../run-time-information-gathering/utils/interactions/inputValueInteraction.js --analysis ../run-time-information-gathering/utils/interactions/methodCallInteraction.js --analysis ../run-time-information-gathering/utils/interactions/putFieldInteraction.js --analysis ../run-time-information-gathering/utils/interactions/usedAsArgumentInteraction.js --analysis ../run-time-information-gathering/utils/interactions/convertedToInteraction.js --analysis ../run-time-information-gathering/utils/interactions/operatorInteraction.js --analysis ../run-time-information-gathering/utils/operators/operatorInteractionBuilder.js --analysis ../run-time-information-gathering/analysis/analysis.js --analysis ../run-time-information-gathering/analysis/callbacks/functionEnter.js --analysis ../run-time-information-gathering/analysis/callbacks/functionExit.js --analysis ../run-time-information-gathering/analysis/callbacks/declare.js --analysis ../run-time-information-gathering/analysis/callbacks/invokeFunPre.js --analysis ../run-time-information-gathering/analysis/callbacks/invokeFun.js --analysis ../run-time-information-gathering/analysis/callbacks/getField.js --analysis ../run-time-information-gathering/analysis/callbacks/putFieldPre.js --analysis ../run-time-information-gathering/analysis/callbacks/write.js --analysis ../run-time-information-gathering/analysis/callbacks/binaryPre.js --analysis ../run-time-information-gathering/analysis/callbacks/unaryPre.js --analysis ../run-time-information-gathering/analysis/callbacks/conditional.js --analysis ../run-time-information-gathering/analysis/callbacks/literal.js "
        
#+ target + " > " + target_dir + "output.json"
analysis_files = []

# Get analysis file paths
for item in node.split():
        if('../run-time-information-gathering' in item):
                analysis_files.append(item)


# Append analysis files
analysis_output = "../abs/Jalangi/analysis_complete.js"

# Read every analysis file and write it to analysis 
for file_path in analysis_files:
        path = os.path.abspath(file_path)
        analysis_file = open(path, 'r')
        analysis_file_source = analysis_file.read()
        with open(os.path.abspath(analysis_output), "a") as output_file:
                output_file.write(analysis_file_source)
