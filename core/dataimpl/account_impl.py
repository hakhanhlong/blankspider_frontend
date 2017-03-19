from ..database.account import ACCOUNTS


def get_by_username(username):
    ac = ACCOUNTS.objects.get_or_404(username=username)
    return ac

