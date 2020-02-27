from core.base.model.AliceSkill import AliceSkill
from core.dialog.model.DialogSession import DialogSession
from core.util.Decorators import IntentHandler


class RobotHead(AliceSkill):
	"""
	Author: rickmini
	Description: Move 2 servos in response to look (left,right,up,down,cener)
	"""

	@IntentHandler('MyIntentName')
	def dummyIntent(self, session: DialogSession, **_kwargs):
		pass
