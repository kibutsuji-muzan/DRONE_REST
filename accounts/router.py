
class AccountsRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """
    router_verbose_names = {'User', 'VerificationDevice','User Profile','Profile Image','User Type'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to accounts.
        """
        if model._meta.verbose_name in self.router_verbose_names:
            return 'accounts'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to accounts.
        """
        if model._meta.verbose_name in self.router_verbose_names:
            return 'accounts'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if (
            obj1._meta.verbose_name in self.router_verbose_names or
            obj2._meta.verbose_name in self.router_verbose_names
        ):
           return True
        return None

    def allow_migrate(self, db, verbose_name, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'accounts' database.
        """
        if verbose_name in self.router_verbose_names:
            return db == 'accounts'
        return None