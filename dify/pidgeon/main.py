from dify_plugin import DifyPluginEnv, Plugin

# Wait for Code holds a request open for up to 280 seconds.
plugin = Plugin(DifyPluginEnv(MAX_REQUEST_TIMEOUT=300))

if __name__ == "__main__":
    plugin.run()
