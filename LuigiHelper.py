import luigi
import os

class LuigiTaskRemoveFileBeforeUpdate(luigi.Task):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        outputs = luigi.task.flatten(self.output())
        for out in outputs:
            if out.exists():
                os.remove(self.output().path)