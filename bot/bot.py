from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.dialogs import Dialog

class Bot(ActivityHandler):
    def __init__(self, dialog: Dialog):
        self.dialog = dialog

    async def on_message_activity(self, turn_context: TurnContext):
        await self.dialog.run(turn_context, self.dialog_state)

    async def on_turn(self, turn_context: TurnContext):
        await super().on_turn(turn_context)
        await self.dialog_state.save_changes(turn_context, False)