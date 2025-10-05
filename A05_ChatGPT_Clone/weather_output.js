const data = [
    {
        "new_agent": {
            "name": "Assistant Agent",
            "handoff_description": null,
            "tools": [
                {
                    "user_location": null,
                    "filters": null,
                    "search_context_size": "medium"
                }
            ],
            "mcp_servers": [],
            "mcp_config": {},
            "instructions": "You are a helpful assistant. Use tools when needed to answer questions.",
            "prompt": null,
            "handoffs": [],
            "model": null,
            "model_settings": {
                "temperature": null,
                "top_p": null,
                "frequency_penalty": null,
                "presence_penalty": null,
                "tool_choice": null,
                "parallel_tool_calls": null,
                "truncation": null,
                "max_tokens": null,
                "reasoning": null,
                "verbosity": null,
                "metadata": null,
                "store": null,
                "include_usage": null,
                "response_include": null,
                "top_logprobs": null,
                "extra_query": null,
                "extra_body": null,
                "extra_headers": null,
                "extra_args": null
            },
            "input_guardrails": [],
            "output_guardrails": [],
            "output_type": null,
            "hooks": null,
            "tool_use_behavior": "run_llm_again",
            "reset_tool_choice": true
        },
        "type": "agent_updated_stream_event"
    },
    {
        "data": {
            "response": {
                "id": "resp_03dd4e218c2ea6eb0068e1eb49ffc0819181061e1ec436732f",
                "created_at": 1759636298.0,
                "error": null,
                "incomplete_details": null,
                "instructions": "You are a helpful assistant. Use tools when needed to answer questions.",
                "metadata": {},
                "model": "gpt-4.1-2025-04-14",
                "object": "response",
                "output": [],
                "parallel_tool_calls": true,
                "temperature": 1.0,
                "tool_choice": "auto",
                "tools": [
                    {
                        "type": "web_search",
                        "filters": null,
                        "search_context_size": "medium",
                        "user_location": {
                            "city": null,
                            "country": "US",
                            "region": null,
                            "timezone": null,
                            "type": "approximate"
                        }
                    }
                ],
                "top_p": 1.0,
                "background": false,
                "conversation": null,
                "max_output_tokens": null,
                "max_tool_calls": null,
                "previous_response_id": null,
                "prompt": null,
                "prompt_cache_key": null,
                "reasoning": {
                    "effort": null,
                    "generate_summary": null,
                    "summary": null
                },
                "safety_identifier": null,
                "service_tier": "auto",
                "status": "in_progress",
                "text": {
                    "format": {
                        "type": "text"
                    },
                    "verbosity": "medium"
                },
                "top_logprobs": 0,
                "truncation": "disabled",
                "usage": null,
                "user": null,
                "store": true
            },
            "sequence_number": 0,
            "type": "response.created"
        },
        "type": "🚀 raw_response_event"
    },
    {
        "data": {
            "response": {
                "id": "resp_03dd4e218c2ea6eb0068e1eb49ffc0819181061e1ec436732f",
                "created_at": 1759636298.0,
                "error": null,
                "incomplete_details": null,
                "instructions": "You are a helpful assistant. Use tools when needed to answer questions.",
                "metadata": {},
                "model": "gpt-4.1-2025-04-14",
                "object": "response",
                "output": [],
                "parallel_tool_calls": true,
                "temperature": 1.0,
                "tool_choice": "auto",
                "tools": [
                    {
                        "type": "web_search",
                        "filters": null,
                        "search_context_size": "medium",
                        "user_location": {
                            "city": null,
                            "country": "US",
                            "region": null,
                            "timezone": null,
                            "type": "approximate"
                        }
                    }
                ],
                "top_p": 1.0,
                "background": false,
                "conversation": null,
                "max_output_tokens": null,
                "max_tool_calls": null,
                "previous_response_id": null,
                "prompt": null,
                "prompt_cache_key": null,
                "reasoning": {
                    "effort": null,
                    "generate_summary": null,
                    "summary": null
                },
                "safety_identifier": null,
                "service_tier": "auto",
                "status": "in_progress",
                "text": {
                    "format": {
                        "type": "text"
                    },
                    "verbosity": "medium"
                },
                "top_logprobs": 0,
                "truncation": "disabled",
                "usage": null,
                "user": null,
                "store": true
            },
            "sequence_number": 1,
            "type": "response.in_progress"
        },
        "type": "🚀 raw_response_event"
    },
    {
        "data": {
            "item": {
                "id": "ws_03dd4e218c2ea6eb0068e1eb4a9a088191b4ebe88e5624413c",
                "action": {
                    "query": null,
                    "type": "search",
                    "sources": null
                },
                "status": "in_progress",
                "type": "web_search_call"
            },
            "output_index": 0,
            "sequence_number": 2,
            "type": "response.output_item.added"
        },
        "type": "🚀 raw_response_event"
    },
    {
        "data": {
            "item_id": "ws_03dd4e218c2ea6eb0068e1eb4a9a088191b4ebe88e5624413c",
            "output_index": 0,
            "sequence_number": 3,
            "type": "response.web_search_call.in_progress"
        },
        "type": "🚀 raw_response_event"
    },
    {
        "data": {
            "item_id": "ws_03dd4e218c2ea6eb0068e1eb4a9a088191b4ebe88e5624413c",
            "output_index": 0,
            "sequence_number": 4,
            "type": "response.web_search_call.searching"
        },
        "type": "🚀 raw_response_event"
    },
    {
        "data": {
            "item_id": "ws_03dd4e218c2ea6eb0068e1eb4a9a088191b4ebe88e5624413c",
            "output_index": 0,
            "sequence_number": 5,
            "type": "response.web_search_call.completed"
        },
        "type": "🚀 raw_response_event"
    },
    {
        "name": "🔎 tool_called",
        "item": {
            "agent": {
                "name": "Assistant Agent",
                "handoff_description": null,
                "tools": [
                    {
                        "user_location": null,
                        "filters": null,
                        "search_context_size": "medium"
                    }
                ],
                "mcp_servers": [],
                "mcp_config": {},
                "instructions": "You are a helpful assistant. Use tools when needed to answer questions.",
                "prompt": null,
                "handoffs": [],
                "model": null,
                "model_settings": {
                    "temperature": null,
                    "top_p": null,
                    "frequency_penalty": null,
                    "presence_penalty": null,
                    "tool_choice": null,
                    "parallel_tool_calls": null,
                    "truncation": null,
                    "max_tokens": null,
                    "reasoning": null,
                    "verbosity": null,
                    "metadata": null,
                    "store": null,
                    "include_usage": null,
                    "response_include": null,
                    "top_logprobs": null,
                    "extra_query": null,
                    "extra_body": null,
                    "extra_headers": null,
                    "extra_args": null
                },
                "input_guardrails": [],
                "output_guardrails": [],
                "output_type": null,
                "hooks": null,
                "tool_use_behavior": "run_llm_again",
                "reset_tool_choice": true
            },
            "raw_item": { 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
                "id": "ws_03dd4e218c2ea6eb0068e1eb4a9a088191b4ebe88e5624413c",
                "action": {
                    "query": "🔥🔥🔥🔥 weather in Madrid 🔥🔥🔥🔥 ",
                    "type": "search",
                    "sources": null
                },
                "status": "completed",
                "type": "web_search_call"
            },
            "type": "tool_call_item"
        },
        "type": "run_item_stream_event"
    },
    {
        "data": {
            "item": {
                "id": "ws_03dd4e218c2ea6eb0068e1eb4a9a088191b4ebe88e5624413c",
                "action": {
                    "query": "🔥🔥🔥🔥 weather in Madrid 🔥🔥🔥🔥 ",
                    "type": "search",
                    "sources": null
                },
                "status": "completed",
                "type": "web_search_call"
            },
            "output_index": 0,
            "sequence_number": 6,
            "type": "response.output_item.done"
        },
        "type": "🚀 raw_response_event"
    },
    {
        "data": {
            "item": {
                "id": "msg_03dd4e218c2ea6eb0068e1eb4b66b481918b9972fb59fbabcb",
                "content": [],
                "role": "assistant",
                "status": "in_progress",
                "type": "message"
            },
            "output_index": 1,
            "sequence_number": 7,
            "type": "response.output_item.added"
        },
        "type": "🚀 raw_response_event"
    },
    {
        "data": {
            "content_index": 0,
            "item_id": "msg_03dd4e218c2ea6eb0068e1eb4b66b481918b9972fb59fbabcb",
            "output_index": 1,
            "part": {
                "annotations": [],
                "text": "",
                "type": "output_text",
                "logprobs": []
            },
            "sequence_number": 8,
            "type": "response.content_part.added"
        },
        "type": "🚀 raw_response_event"
    },
    {
        "data": {
            "content_index": 0,
            "delta": "Hello! I'm doing well\u2014thank you for asking.\n",
            "item_id": "msg_03dd4e218c2ea6eb0068e1eb4b66b481918b9972fb59fbabcb",
            "logprobs": [],
            "output_index": 1,
            "sequence_number": 9,
            "type": "✅ response.output_text.delta",
            "obfuscation": "bBvE"
        },
        "type": "🚀 raw_response_event"
    },
    {
        "data": {
            "content_index": 0,
            "delta": "\nHere\u2019s the current weather in Madrid, the capital of Spain",
            "item_id": "msg_03dd4e218c2ea6eb0068e1eb4b66b481918b9972fb59fbabcb",
            "logprobs": [],
            "output_index": 1,
            "sequence_number": 10,
            "type": "✅ response.output_text.delta",
            "obfuscation": "uRgr8"
        },
        "type": "🚀 raw_response_event"
    },
    {
        "data": {
            "content_index": 0,
            "delta": ":\n\nWeather in Madrid (October 5, 2025",
            "item_id": "msg_03dd4e218c2ea6eb0068e1eb4b66b481918b9972fb59fbabcb",
            "logprobs": [],
            "output_index": 1,
            "sequence_number": 11,
            "type": "✅ response.output_text.delta",
            "obfuscation": "ZUMCCebqxGI"
        },
        "type": "🚀 raw_response_event"
    },
    {
        "data": {
            "content_index": 0,
            "delta": "):\n- It is currently partly cloudy with a temperature of approximately 61\u202f",
            "item_id": "msg_03dd4e218c2ea6eb0068e1eb4b66b481918b9972fb59fbabcb",
            "logprobs": [],
            "output_index": 1,
            "sequence_number": 12,
            "type": "✅ response.output_text.delta",
            "obfuscation": "RHpcrE"
        },
        "type": "🚀 raw_response_event"
    },
    {
        "data": {
            "content_index": 0,
            "delta": "\u00b0F (16\u202f\u00b0C).",
            "item_id": "msg_03dd4e218c2ea6eb0068e1eb4b66b481918b9972fb59fbabcb",
            "logprobs": [],
            "output_index": 1,
            "sequence_number": 13,
            "type": "✅ response.output_text.delta",
            "obfuscation": "0TgaX"
        },
        "type": "🚀 raw_response_event"
    },
    {
        "data": {
            "content_index": 0,
            "delta": "  \n- As the day progresses,",
            "item_id": "msg_03dd4e218c2ea6eb0068e1eb4b66b481918b9972fb59fbabcb",
            "logprobs": [],
            "output_index": 1,
            "sequence_number": 14,
            "type": "✅ response.output_text.delta",
            "obfuscation": "s8di3"
        },
        "type": "🚀 raw_response_event"
    },
    {
        "data": {
            "content_index": 0,
            "delta": " the skies are expected to clear, leading to plenty of sunshine",
            "item_id": "msg_03dd4e218c2ea6eb0068e1eb4b66b481918b9972fb59fbabcb",
            "logprobs": [],
            "output_index": 1,
            "sequence_number": 15,
            "type": "✅ response.output_text.delta",
            "obfuscation": "n"
        },
        "type": "🚀 raw_response_event"
    },
    {
        "data": {
            "content_index": 0,
            "delta": " into the afternoon. Temperatures will gradually warm",
            "item_id": "msg_03dd4e218c2ea6eb0068e1eb4b66b481918b9972fb59fbabcb",
            "logprobs": [],
            "output_index": 1,
            "sequence_number": 16,
            "type": "✅ response.output_text.delta",
            "obfuscation": "ndxdqpScH7P"
        },
        "type": "🚀 raw_response_event"
    },
    {
        "data": {
            "content_index": 0,
            "delta": ", rising from around 60\u202f\u00b0F (16\u202f\u00b0C",
            "item_id": "msg_03dd4e218c2ea6eb0068e1eb4b66b481918b9972fb59fbabcb",
            "logprobs": [],
            "output_index": 1,
            "sequence_number": 17,
            "type": "✅ response.output_text.delta",
            "obfuscation": "wcuSeQ1eP1Ffx6E"
        },
        "type": "🚀 raw_response_event"
    },
    {
        "data": {
            "content_index": 0,
            "delta": ") in the morning to a high of approximately 77\u202f",
            "item_id": "msg_03dd4e218c2ea6eb0068e1eb4b66b481918b9972fb59fbabcb",
            "logprobs": [],
            "output_index": 1,
            "sequence_number": 18,
            "type": "✅ response.output_text.delta",
            "obfuscation": "1"
        },
        "type": "🚀 raw_response_event"
    },
    {
        "data": {
            "content_index": 0,
            "delta": "\u00b0F (25\u202f\u00b0C) by mid-afternoon.",
            "item_id": "msg_03dd4e218c2ea6eb0068e1eb4b66b481918b9972fb59fbabcb",
            "logprobs": [],
            "output_index": 1,
            "sequence_number": 19,
            "type": "✅ response.output_text.delta",
            "obfuscation": "J8Cc"
        },
        "type": "🚀 raw_response_event"
    },
    {
        "data": {
            "content_index": 0,
            "delta": "\n\nIf",
            "item_id": "msg_03dd4e218c2ea6eb0068e1eb4b66b481918b9972fb59fbabcb",
            "logprobs": [],
            "output_index": 1,
            "sequence_number": 20,
            "type": "✅ response.output_text.delta",
            "obfuscation": "Hy7LRt18bpEo"
        },
        "type": "🚀 raw_response_event"
    },
    {
        "data": {
            "content_index": 0,
            "delta": " you\u2019d like a weather forecast for additional days, upcoming events, or suggestions",
            "item_id": "msg_03dd4e218c2ea6eb0068e1eb4b66b481918b9972fb59fbabcb",
            "logprobs": [],
            "output_index": 1,
            "sequence_number": 21,
            "type": "✅ response.output_text.delta",
            "obfuscation": "kJectissMpCs6"
        },
        "type": "🚀 raw_response_event"
    },
    {
        "data": {
            "content_index": 0,
            "delta": " on what to wear for certain conditions, just let me know!",
            "item_id": "msg_03dd4e218c2ea6eb0068e1eb4b66b481918b9972fb59fbabcb",
            "logprobs": [],
            "output_index": 1,
            "sequence_number": 22,
            "type": "✅ response.output_text.delta",
            "obfuscation": "pIkNbd"
        },
        "type": "🚀 raw_response_event"
    },
    {
        "data": {
            "content_index": 0,
            "item_id": "msg_03dd4e218c2ea6eb0068e1eb4b66b481918b9972fb59fbabcb",
            "logprobs": [],
            "output_index": 1,
            "sequence_number": 23,
            "text": "Hello! I'm doing well\u2014thank you for asking.\n\nHere\u2019s the current weather in Madrid, the capital of Spain:\n\nWeather in Madrid (October 5, 2025):\n- It is currently partly cloudy with a temperature of approximately 61\u202f\u00b0F (16\u202f\u00b0C).  \n- As the day progresses, the skies are expected to clear, leading to plenty of sunshine into the afternoon. Temperatures will gradually warm, rising from around 60\u202f\u00b0F (16\u202f\u00b0C) in the morning to a high of approximately 77\u202f\u00b0F (25\u202f\u00b0C) by mid-afternoon.\n\nIf you\u2019d like a weather forecast for additional days, upcoming events, or suggestions on what to wear for certain conditions, just let me know!",
            "type": "response.output_text.done"
        },
        "type": "🚀 raw_response_event"
    },
    {
        "data": {
            "content_index": 0,
            "item_id": "msg_03dd4e218c2ea6eb0068e1eb4b66b481918b9972fb59fbabcb",
            "output_index": 1,
            "part": {
                "annotations": [],
                "text": "Hello! I'm doing well\u2014thank you for asking.\n\nHere\u2019s the current weather in Madrid, the capital of Spain:\n\nWeather in Madrid (October 5, 2025):\n- It is currently partly cloudy with a temperature of approximately 61\u202f\u00b0F (16\u202f\u00b0C).  \n- As the day progresses, the skies are expected to clear, leading to plenty of sunshine into the afternoon. Temperatures will gradually warm, rising from around 60\u202f\u00b0F (16\u202f\u00b0C) in the morning to a high of approximately 77\u202f\u00b0F (25\u202f\u00b0C) by mid-afternoon.\n\nIf you\u2019d like a weather forecast for additional days, upcoming events, or suggestions on what to wear for certain conditions, just let me know!",
                "type": "output_text",
                "logprobs": []
            },
            "sequence_number": 24,
            "type": "response.content_part.done"
        },
        "type": "🚀 raw_response_event"
    },
    {
        "data": {
            "item": {
                "id": "msg_03dd4e218c2ea6eb0068e1eb4b66b481918b9972fb59fbabcb",
                "content": [
                    {
                        "annotations": [],
                        "text": "Hello! I'm doing well\u2014thank you for asking.\n\nHere\u2019s the current weather in Madrid, the capital of Spain:\n\nWeather in Madrid (October 5, 2025):\n- It is currently partly cloudy with a temperature of approximately 61\u202f\u00b0F (16\u202f\u00b0C).  \n- As the day progresses, the skies are expected to clear, leading to plenty of sunshine into the afternoon. Temperatures will gradually warm, rising from around 60\u202f\u00b0F (16\u202f\u00b0C) in the morning to a high of approximately 77\u202f\u00b0F (25\u202f\u00b0C) by mid-afternoon.\n\nIf you\u2019d like a weather forecast for additional days, upcoming events, or suggestions on what to wear for certain conditions, just let me know!",
                        "type": "output_text",
                        "logprobs": []
                    }
                ],
                "role": "assistant",
                "status": "completed",
                "type": "message"
            },
            "output_index": 1,
            "sequence_number": 25,
            "type": "response.output_item.done"
        },
        "type": "🚀 raw_response_event"
    },
    {
        "data": {
            "response": {
                "id": "resp_03dd4e218c2ea6eb0068e1eb49ffc0819181061e1ec436732f",
                "created_at": 1759636298.0,
                "error": null,
                "incomplete_details": null,
                "instructions": "You are a helpful assistant. Use tools when needed to answer questions.",
                "metadata": {},
                "model": "gpt-4.1-2025-04-14",
                "object": "response",
                "output": [
                    {
                        "id": "ws_03dd4e218c2ea6eb0068e1eb4a9a088191b4ebe88e5624413c",
                        "action": {
                            "query": "weather in Madrid",
                            "type": "search",
                            "sources": null
                        },
                        "status": "completed",
                        "type": "web_search_call"
                    },
                    {
                        "id": "msg_03dd4e218c2ea6eb0068e1eb4b66b481918b9972fb59fbabcb",
                        "content": [
                            {
                                "annotations": [],
                                "text": "Hello! I'm doing well\u2014thank you for asking.\n\nHere\u2019s the current weather in Madrid, the capital of Spain:\n\nWeather in Madrid (October 5, 2025):\n- It is currently partly cloudy with a temperature of approximately 61\u202f\u00b0F (16\u202f\u00b0C).  \n- As the day progresses, the skies are expected to clear, leading to plenty of sunshine into the afternoon. Temperatures will gradually warm, rising from around 60\u202f\u00b0F (16\u202f\u00b0C) in the morning to a high of approximately 77\u202f\u00b0F (25\u202f\u00b0C) by mid-afternoon.\n\nIf you\u2019d like a weather forecast for additional days, upcoming events, or suggestions on what to wear for certain conditions, just let me know!",
                                "type": "output_text",
                                "logprobs": []
                            }
                        ],
                        "role": "assistant",
                        "status": "completed",
                        "type": "message"
                    }
                ],
                "parallel_tool_calls": true,
                "temperature": 1.0,
                "tool_choice": "auto",
                "tools": [
                    {
                        "type": "web_search",
                        "filters": null,
                        "search_context_size": "medium",
                        "user_location": {
                            "city": null,
                            "country": "US",
                            "region": null,
                            "timezone": null,
                            "type": "approximate"
                        }
                    }
                ],
                "top_p": 1.0,
                "background": false,
                "conversation": null,
                "max_output_tokens": null,
                "max_tool_calls": null,
                "previous_response_id": null,
                "prompt": null,
                "prompt_cache_key": null,
                "reasoning": {
                    "effort": null,
                    "generate_summary": null,
                    "summary": null
                },
                "safety_identifier": null,
                "service_tier": "default",
                "status": "completed",
                "text": {
                    "format": {
                        "type": "text"
                    },
                    "verbosity": "medium"
                },
                "top_logprobs": 0,
                "truncation": "disabled",
                "usage": {
                    "input_tokens": 2711,
                    "input_tokens_details": {
                        "cached_tokens": 0
                    },
                    "output_tokens": 205,
                    "output_tokens_details": {
                        "reasoning_tokens": 0
                    },
                    "total_tokens": 2916
                },
                "user": null,
                "store": true
            },
            "sequence_number": 26,
            "type": "response.completed         🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉"
        },
        "type": "🚀 raw_response_event"
    },
    {
        "name": "message_output_created",
        "item": {
            "agent": {
                "name": "Assistant Agent",
                "handoff_description": null,
                "tools": [
                    {
                        "user_location": null,
                        "filters": null,
                        "search_context_size": "medium"
                    }
                ],
                "mcp_servers": [],
                "mcp_config": {},
                "instructions": "You are a helpful assistant. Use tools when needed to answer questions.",
                "prompt": null,
                "handoffs": [],
                "model": null,
                "model_settings": {
                    "temperature": null,
                    "top_p": null,
                    "frequency_penalty": null,
                    "presence_penalty": null,
                    "tool_choice": null,
                    "parallel_tool_calls": null,
                    "truncation": null,
                    "max_tokens": null,
                    "reasoning": null,
                    "verbosity": null,
                    "metadata": null,
                    "store": null,
                    "include_usage": null,
                    "response_include": null,
                    "top_logprobs": null,
                    "extra_query": null,
                    "extra_body": null,
                    "extra_headers": null,
                    "extra_args": null
                },
                "input_guardrails": [],
                "output_guardrails": [],
                "output_type": null,
                "hooks": null,
                "tool_use_behavior": "run_llm_again",
                "reset_tool_choice": true
            },
            "raw_item": { 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
                "id": "msg_03dd4e218c2ea6eb0068e1eb4b66b481918b9972fb59fbabcb",
                "content": [
                    {
                        "annotations": [],
                        "text": "Hello! I'm doing well\u2014thank you for asking.\n\nHere\u2019s the current weather in Madrid, the capital of Spain:\n\nWeather in Madrid (October 5, 2025):\n- It is currently partly cloudy with a temperature of approximately 61\u202f\u00b0F (16\u202f\u00b0C).  \n- As the day progresses, the skies are expected to clear, leading to plenty of sunshine into the afternoon. Temperatures will gradually warm, rising from around 60\u202f\u00b0F (16\u202f\u00b0C) in the morning to a high of approximately 77\u202f\u00b0F (25\u202f\u00b0C) by mid-afternoon.\n\nIf you\u2019d like a weather forecast for additional days, upcoming events, or suggestions on what to wear for certain conditions, just let me know!",
                        "type": "output_text",
                        "logprobs": []
                    }
                ],
                "role": "assistant",
                "status": "completed",
                "type": "message"
            },
            "type": "message_output_item"
        },
        "type": "run_item_stream_event"
    }
]
