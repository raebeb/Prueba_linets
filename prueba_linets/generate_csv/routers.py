class GenerateCsvRouter(object): 
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'generate_csv':
            return 'legacy_db'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'generate_csv':
            return 'legacy_db'
        return 'default'
    
    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'generate_csv' and obj2._meta.app_label == 'generate_csv':
            return True
        elif 'generate_csv' not in [obj1._meta.app_label, obj2._meta.app_label]: 
            return True
        return False
    
    def allow_syncdb(self, db, model):
        if db == 'legacy_db' or model._meta.app_label == "generate_csv":
            return False 
        else: 
            return True