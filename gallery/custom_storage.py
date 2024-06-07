from django.core.files.storage import FileSystemStorage # type: ignore

class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        # 동일한 이름의 파일이 존재하면 기존 파일을 삭제
        if self.exists(name):
            self.delete(name)
        return name