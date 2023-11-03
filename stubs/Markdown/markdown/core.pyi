from collections.abc import Callable, Mapping, Sequence
from typing import Any, ClassVar, Protocol
from typing_extensions import Literal, Self
from xml.etree.ElementTree import Element

from . import blockparser, inlinepatterns, postprocessors, preprocessors, treeprocessors
from .extensions import Extension
from .util import HtmlStash, Registry

# TODO: The following protocols can be replaced by their counterparts from
# codecs, once they have been propagated to all type checkers.
class _WritableStream(Protocol):
    def write(self, __data: bytes) -> object: ...
    def seek(self, __offset: int, __whence: int) -> object: ...
    def close(self) -> object: ...

class _ReadableStream(Protocol):
    def read(self, __size: int = ...) -> bytes: ...
    def seek(self, __offset: int, __whence: int) -> object: ...
    def close(self) -> object: ...

class Markdown:
    preprocessors: Registry[preprocessors.Preprocessor]
    inlinePatterns: Registry[inlinepatterns.InlineProcessor | inlinepatterns.Pattern]
    treeprocessors: Registry[treeprocessors.Treeprocessor]
    postprocessors: Registry[postprocessors.Postprocessor]
    parser: blockparser.BlockParser
    htmlStash: HtmlStash
    output_formats: ClassVar[dict[Literal["xhtml", "html"], Callable[[Element], str]]]
    output_format: Literal["xhtml", "html"]
    serializer: Callable[[Element], str]
    tab_length: int
    block_level_elements: list[str]
    registeredExtensions: list[Extension]
    ESCAPED_CHARS: list[str]
    def __init__(
        self,
        *,
        extensions: Sequence[str | Extension] | None = ...,
        extension_configs: Mapping[str, Mapping[str, Any]] | None = ...,
        output_format: Literal["xhtml", "html"] | None = ...,
        tab_length: int | None = ...,
    ) -> None: ...
    def build_parser(self) -> Self: ...
    def registerExtensions(self, extensions: Sequence[Extension | str], configs: Mapping[str, dict[str, Any]]) -> Self: ...
    def build_extension(self, ext_name: str, configs: Mapping[str, Any]) -> Extension: ...
    def registerExtension(self, extension: Extension) -> Self: ...
    def reset(self) -> Self: ...
    def set_output_format(self, format: Literal["xhtml", "html"]) -> Self: ...
    def is_block_level(self, tag: object) -> bool: ...
    def convert(self, source: str) -> str: ...
    def convertFile(
        self, input: str | _ReadableStream | None = None, output: str | _WritableStream | None = None, encoding: str | None = None
    ) -> Self: ...

def markdown(
    text: str,
    *,
    extensions: Sequence[str | Extension] | None = ...,
    extension_configs: Mapping[str, Mapping[str, Any]] | None = ...,
    output_format: Literal["xhtml", "html"] | None = ...,
    tab_length: int | None = ...,
) -> str: ...
def markdownFromFile(
    *,
    input: str | _ReadableStream | None = ...,
    output: str | _WritableStream | None = ...,
    encoding: str | None = ...,
    extensions: Sequence[str | Extension] | None = ...,
    extension_configs: Mapping[str, Mapping[str, Any]] | None = ...,
    output_format: Literal["xhtml", "html"] | None = ...,
    tab_length: int | None = ...,
) -> None: ...
