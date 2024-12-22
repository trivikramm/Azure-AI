from botbuilder.dialogs import ComponentDialog, WaterfallDialog, WaterfallStepContext
from botbuilder.core import MessageFactory

class CustomerServiceDialog(ComponentDialog):
    def __init__(self, luis_service):
        super(CustomerServiceDialog, self).__init__(CustomerServiceDialog.__name__)
        self.luis_service = luis_service
        self.add_dialog(WaterfallDialog("WFDialog", [self.process_step]))
        self.initial_dialog_id = "WFDialog"

    async def process_step(self, step_context: WaterfallStepContext):
        luis_result = await self.luis_service.recognize(step_context.context)
        intent = luis_result.get_top_scoring_intent().intent
        if intent == "GetHelp":
            await step_context.context.send_activity(MessageFactory.text("Sure, I can help you with that."))
        else:
            await step_context.context.send_activity(MessageFactory.text("I'm not sure how to help with that."))
        return await step_context.end_dialog()