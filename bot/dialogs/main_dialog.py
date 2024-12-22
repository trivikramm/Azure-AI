from botbuilder.dialogs import ComponentDialog, DialogSet, DialogTurnStatus, WaterfallDialog, WaterfallStepContext
from botbuilder.core import MessageFactory

class MainDialog(ComponentDialog):
    def __init__(self, customer_service_dialog):
        super(MainDialog, self).__init__(MainDialog.__name__)
        self.add_dialog(WaterfallDialog("WFDialog", [self.intro_step, self.act_step]))
        self.add_dialog(customer_service_dialog)
        self.initial_dialog_id = "WFDialog"

    async def intro_step(self, step_context: WaterfallStepContext):
        return await step_context.prompt("TextPrompt", MessageFactory.text("How can I assist you today?"))

    async def act_step(self, step_context: WaterfallStepContext):
        return await step_context.begin_dialog("CustomerServiceDialog")