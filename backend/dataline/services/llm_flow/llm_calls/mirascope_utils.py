from typing import Callable, Literal, ParamSpec, TypeVar

from mirascope.core import openai
from mirascope.core.base import BaseMessageParam
from openai import OpenAI
from pydantic import BaseModel

from dataline.config import config


class GeminiClientOptions(BaseModel):
    api_key: str
    base_url: str | None = None


AvailableModels = (
    Literal["gemini-3.1-pro-preview"]
    | Literal["gemini-3.1-flash-lite-preview"]
    | Literal["gemini-2.0-flash"]
    | Literal["gemini-2.0-flash-lite"]
)

_T = TypeVar("_T", bound=BaseModel)
P = ParamSpec("P")


def call(
    model: AvailableModels,
    response_model: type[_T],
    prompt_fn: Callable[P, list[BaseMessageParam]],
    client_options: GeminiClientOptions,
) -> Callable[P, _T]:
    return openai.call(
        model=model,
        response_model=response_model,
        json_mode=True,
        client=OpenAI(
            api_key=client_options.api_key,
            base_url=client_options.base_url or config.default_base_url,
        ),
    )(prompt_fn)
