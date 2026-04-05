import logging
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, SecretStr, field_serializer

logger = logging.getLogger(__name__)


class UserUpdateIn(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=250)
    gemini_api_key: Optional[SecretStr] = Field(None, min_length=4)
    api_base_url: str | None = Field(None, min_length=4)
    langsmith_api_key: Optional[SecretStr] = Field(None, min_length=4)
    preferred_model: Optional[str] = None
    sentry_enabled: Optional[bool] = None
    analytics_enabled: Optional[bool] = None
    hide_sql_preference: Optional[bool] = None

    @field_serializer("gemini_api_key")
    def dump_gemini_api_key(self, v: SecretStr | None) -> str | None:
        return v.get_secret_value() if v else None

    @field_serializer("langsmith_api_key")
    def dump_langsmith_api_key(self, v: SecretStr | None) -> str | None:
        return v.get_secret_value() if v else None


class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: Optional[str] = None
    gemini_api_key: Optional[SecretStr] = None
    api_base_url: str | None = None
    langsmith_api_key: Optional[SecretStr] = None
    preferred_model: Optional[str] = None
    sentry_enabled: bool
    analytics_enabled: Optional[bool] = None
    hide_sql_preference: Optional[bool] = None


class UserWithKeys(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: Optional[str] = None

    gemini_api_key: SecretStr
    api_base_url: str | None = None
    langsmith_api_key: SecretStr | None = None
    preferred_model: str
    sentry_enabled: bool
    analytics_enabled: Optional[bool] = None
    hide_sql_preference: Optional[bool] = None


class AvatarOut(BaseModel):
    blob: str
