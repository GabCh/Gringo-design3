from ApplicationRunner import ApplicationRunner
from atlas.context import runtime_contexts
from atlas.infrastructure.context import create_context, discover_contexts


def start_local_debug_app():
    discover_contexts(runtime_contexts)
    context = create_context("QuicksilverContext")
    serviceLocator = context.service_locator()
    serviceLocator.get(ApplicationRunner).run()


if __name__ == "__main__":
    start_local_debug_app()
