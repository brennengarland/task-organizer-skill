from mycroft import MycroftSkill, intent_file_handler


class TaskOrganizer(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('organizer.task.intent')
    def handle_organizer_task(self, message):
        self.speak_dialog('organizer.task')


def create_skill():
    return TaskOrganizer()

