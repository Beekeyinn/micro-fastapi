def get_apps_for_database(apps):
    default_connection = {"default_connection": "default"}
    apps = {
        "models": {
            "models": ["aerich.models"] + [f"apps.{app}.models" for app in apps],
            **default_connection,
        }
    }
    # migrations_sources = ["models"]
    # app_models = {**_aerich}
    # for app in apps:
    #     migrations_sources.append(f"apps.{app}.models")
    #     models = {
    #         f"{app}": {
    #             "models": [f"apps.{app}.models"],
    #             **default_connection,
    #         }
    #     }
    #     app_models.update(models)

    # return app_models, migrations_sources
    return apps
