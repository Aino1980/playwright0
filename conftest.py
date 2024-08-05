import pytest
import re

from playwright.sync_api import Browser, BrowserContext, expect
from pytest_playwright.pytest_playwright import ArtifactsRecorder, CreateContextCallback

from utils.globalMap import GlobalMap
from typing import (
    Any,
    Callable,
    Dict,
    Generator,
    List,
    Literal,
    Optional,
    Protocol,
    Sequence,
    Union,
    Pattern,
    cast,

)

# @pytest.fixture()
# def hello_world():
#     print("hello")
#     yield
#     print("world")
#
#
# @pytest.fixture
# def page(context: BrowserContext) -> Page:
#     print("this is my page")
#     return context.new_page()


@pytest.fixture(scope="session", autouse=True)
def test_init(base_url):
    global_map = GlobalMap()
    global_map.set("baseurl", base_url)
    env = re.search("(https://)(.*)(.ezone.work)", base_url).group(2)
    global_map.set("env", env)


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, pytestconfig: Any):
    width, height = pytestconfig.getoption("--viewport")
    return {
        **browser_context_args,
        "viewport": {
            "width": width,
            "height": height,
        },
        "record_video_size": {
            "width": width,
            "height": height,
        },

    }


def pytest_addoption(parser: Any) -> None:
    group = parser.getgroup("playwright", "Playwright")
    group.addoption(
        "--viewport",
        action="store",
        default=[1440, 900],
        help="viewport size set",
        type=int,
        nargs=2,
    )
    group.addoption(
        "--ui_timeout",
        default=30_000,
        help="locator timeout and expect timeout",
    )


@pytest.fixture(scope="session")
def ui_timeout(pytestconfig):
    timeout = float(pytestconfig.getoption("--ui_timeout"))
    expect.set_options(timeout=timeout)
    return timeout


@pytest.fixture
def new_context(
    browser: Browser,
    browser_context_args: Dict,
    _artifacts_recorder: "ArtifactsRecorder",
    request: pytest.FixtureRequest,
    ui_timeout,
) -> Generator[CreateContextCallback, None, None]:
    browser_context_args = browser_context_args.copy()
    context_args_marker = next(request.node.iter_markers("browser_context_args"), None)
    additional_context_args = context_args_marker.kwargs if context_args_marker else {}
    browser_context_args.update(additional_context_args)
    contexts: List[BrowserContext] = []

    def _new_context(**kwargs: Any) -> BrowserContext:
        context = browser.new_context(**browser_context_args, **kwargs)
        context.set_default_timeout(ui_timeout)
        context.set_default_navigation_timeout(ui_timeout * 2)
        original_close = context.close

        def _close_wrapper(*args: Any, **kwargs: Any) -> None:
            contexts.remove(context)
            _artifacts_recorder.on_will_close_browser_context(context)
            original_close(*args, **kwargs)

        context.close = _close_wrapper
        contexts.append(context)
        _artifacts_recorder.on_did_create_browser_context(context)
        return context

    yield cast(CreateContextCallback, _new_context)
    for context in contexts.copy():
        context.close()


