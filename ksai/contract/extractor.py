# coding=utf-8
# -*- coding: UTF-8 -*-
#
# This file is part of the kernelstudio package.
#
# (c) 2014-2025 zlin <admin@kernelstudio.com>
#
# For the full copyright and license information, please view the LICENSE file
# that was distributed with this source code.
import json
import typing as t

from ksai.contract.prompts import format_contract_extractor_prompt
from ksai.formater import clean_json_response
from ksai.llm.ollama_client import ollama_execute


def contract_content_extractor(host: str, model: str, options: dict[str, t.Any]) -> str | None:
    prompt = options['prompt']
    if not prompt:
        prompt = '请从以下合同文本中提取{rules}相关信息，不要输出重复的内容, 请直接使用JSON格式回答.'

    if prompt and '{rules}' in prompt:
        rules = options['rules']
        if not rules:
            rules = ''
        prompt = prompt.replace('{rules}', rules)

    text = options['text']
    if text:
        try:
            text_json = json.loads(clean_json_response(options['text']))
            if text_json and text_json['text']:
                text = text_json['text']
        except Exception:
            pass
    prompt = format_contract_extractor_prompt(
        prompt,
        text
    )
    options['prompt'] = prompt

    result = ollama_execute(host, model, options)
    if result and "</think>" in result:
        result = result.split("</think>")[1]
    return clean_json_response(result)
