def open_door_card(network_name, model_name, sensor_name, timestamp, sensor_link):
    card = {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
            "type": "AdaptiveCard",
            "version": "1.2",
            "body": [
                {
                    "type": "ColumnSet",
                    "columns": [
                        {
                            "type": "Column",
                            "items": [
                                {
                                    "type": "Image",
                                    "style": "Person",
                                    "url": "https://cdn0.iconfinder.com/data/icons/home-security-2/45/security-02-512.png",
                                    "size": "Medium",
                                    "height": "50px"
                                }
                            ],
                            "width": "auto"
                        },
                        {
                            "type": "Column",
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "text": "Meraki Dashboard Alert",
                                    "weight": "Lighter",
                                    "color": "Accent"
                                },
                                {
                                    "type": "TextBlock",
                                    "weight": "Bolder",
                                    "text": "Open Door Detected!",
                                    "horizontalAlignment": "Left",
                                    "wrap": True,
                                    "color": "Light",
                                    "size": "Large",
                                    "spacing": "Small"
                                }
                            ],
                            "width": "stretch"
                        }
                    ]
                },
                {
                    "type": "ColumnSet",
                    "columns": [
                        {
                            "type": "Column",
                            "width": 35,
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "text": "Network Name:",
                                    "weight": "Bolder",
                                    "color": "Light"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": "Sensor Name:",
                                    "weight": "Bolder",
                                    "color": "Light",
                                    "spacing": "Small"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": "Model:",
                                    "weight": "Bolder",
                                    "color": "Light",
                                    "spacing": "Small"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": "Timestamp:",
                                    "weight": "Bolder",
                                    "color": "Light",
                                    "spacing": "Small"
                                }
                            ]
                        },
                        {
                            "type": "Column",
                            "width": 65,
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "text": network_name,
                                    "color": "Light"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": sensor_name,
                                    "color": "Light",
                                    "weight": "Lighter",
                                    "spacing": "Small"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": model_name,
                                    "weight": "Lighter",
                                    "color": "Light",
                                    "spacing": "Small"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": timestamp,
                                    "weight": "Lighter",
                                    "color": "Light",
                                    "spacing": "Small"
                                }
                            ]
                        }
                    ],
                    "spacing": "Padding",
                    "horizontalAlignment": "Center"
                },
                {
                    "type": "ColumnSet",
                    "columns": [
                        {
                            "type": "Column",
                            "width": "auto",
                            "items": [
                                {
                                    "type": "Image",
                                    "altText": "",
                                    "url": "https://developer.webex.com/images/link-icon.png",
                                    "size": "Small",
                                    "width": "30px"
                                }
                            ],
                            "spacing": "Small"
                        },
                        {
                            "type": "Column",
                            "width": "auto",
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "text": f"[Go to Sensor Dashboard Link]({sensor_link})",
                                    "horizontalAlignment": "Left",
                                    "size": "Medium"
                                }
                            ],
                            "verticalContentAlignment": "Center",
                            "horizontalAlignment": "Left",
                            "spacing": "Small"
                        }
                    ]
                }
            ]
        }
    }

    return card

def snapshot_card(network_name, camera_name, model_name, timestamp, camera_link, snapshot_link):
    card = {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
            "type": "AdaptiveCard",
            "version": "1.2",
            "body": [
                {
                    "type": "ColumnSet",
                    "columns": [
                        {
                            "type": "Column",
                            "items": [
                                {
                                    "type": "Image",
                                    "style": "Person",
                                    "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRspxoQVhoPY_NuCw3-7nPybL_RXJX7STwOOg&usqp=CAU",
                                    "size": "Medium",
                                    "height": "50px"
                                }
                            ],
                            "width": "auto"
                        },
                        {
                            "type": "Column",
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "text": "Meraki Dashboard Alert",
                                    "weight": "Lighter",
                                    "color": "Accent"
                                },
                                {
                                    "type": "TextBlock",
                                    "weight": "Bolder",
                                    "text": "Meraki MV Snapshot",
                                    "horizontalAlignment": "Left",
                                    "wrap": True,
                                    "color": "Light",
                                    "size": "Large",
                                    "spacing": "Small"
                                }
                            ],
                            "width": "stretch"
                        }
                    ]
                },
                {
                    "type": "ColumnSet",
                    "columns": [
                        {
                            "type": "Column",
                            "width": 35,
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "text": "Network Name:",
                                    "weight": "Bolder",
                                    "color": "Light"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": "Camera Name:",
                                    "weight": "Bolder",
                                    "color": "Light",
                                    "spacing": "Small"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": "Model:",
                                    "weight": "Bolder",
                                    "color": "Light",
                                    "spacing": "Small"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": "Timestamp:",
                                    "weight": "Bolder",
                                    "color": "Light",
                                    "spacing": "Small"
                                }
                            ]
                        },
                        {
                            "type": "Column",
                            "width": 65,
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "text": network_name,
                                    "color": "Light"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": camera_name,
                                    "color": "Light",
                                    "weight": "Lighter",
                                    "spacing": "Small"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": model_name,
                                    "weight": "Lighter",
                                    "color": "Light",
                                    "spacing": "Small"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": timestamp,
                                    "weight": "Lighter",
                                    "color": "Light",
                                    "spacing": "Small"
                                }
                            ]
                        }
                    ],
                    "spacing": "Padding",
                    "horizontalAlignment": "Center"
                },
                {
                    "type": "ColumnSet",
                    "columns": [
                        {
                            "type": "Column",
                            "width": "auto",
                            "items": [
                                {
                                    "type": "Image",
                                    "url": snapshot_link
                                }
                            ]
                        }
                    ],
                    "spacing": "Padding",
                    "horizontalAlignment": "Center"
                },
                {
                    "type": "ColumnSet",
                    "columns": [
                        {
                            "type": "Column",
                            "width": "auto",
                            "items": [
                                {
                                    "type": "Image",
                                    "altText": "",
                                    "url": "https://developer.webex.com/images/link-icon.png",
                                    "size": "Small",
                                    "width": "30px"
                                }
                            ],
                            "spacing": "Small"
                        },
                        {
                            "type": "Column",
                            "width": "auto",
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "text": f"[Go to Camera Dashboard Link]({camera_link})",
                                    "horizontalAlignment": "Left",
                                    "size": "Medium"
                                }
                            ],
                            "verticalContentAlignment": "Center",
                            "horizontalAlignment": "Left",
                            "spacing": "Small"
                        }
                    ]
                }
            ]
        }
    }

    return card

def door_timer_card(network_name, model_name, sensor_name, timestamp, sensor_link, elapsed_time):
    card = {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
            "type": "AdaptiveCard",
            "version": "1.2",
            "body": [
                {
                    "type": "ColumnSet",
                    "columns": [
                        {
                            "type": "Column",
                            "items": [
                                {
                                    "type": "Image",
                                    "style": "Person",
                                    "url": "https://static.thenounproject.com/png/141571-200.png",
                                    "size": "Medium",
                                    "height": "50px"
                                }
                            ],
                            "width": "auto"
                        },
                        {
                            "type": "Column",
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "text": "Meraki Dashboard Alert",
                                    "weight": "Lighter",
                                    "color": "Accent"
                                },
                                {
                                    "type": "TextBlock",
                                    "weight": "Bolder",
                                    "text": "Door open for too long!",
                                    "horizontalAlignment": "Left",
                                    "wrap": True,
                                    "color": "Light",
                                    "size": "Large",
                                    "spacing": "Small"
                                }
                            ],
                            "width": "stretch"
                        }
                    ]
                },
                {
                    "type": "ColumnSet",
                    "columns": [
                        {
                            "type": "Column",
                            "width": 35,
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "text": "Network Name:",
                                    "weight": "Bolder",
                                    "color": "Light"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": "Sensor Name:",
                                    "weight": "Bolder",
                                    "color": "Light",
                                    "spacing": "Small"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": "Model:",
                                    "weight": "Bolder",
                                    "color": "Light",
                                    "spacing": "Small"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": "Initial Alert:",
                                    "weight": "Bolder",
                                    "color": "Light",
                                    "spacing": "Small"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": "Alerting for:",
                                    "weight": "Bolder",
                                    "color": "Light",
                                    "spacing": "Small"
                                }
                            ]
                        },
                        {
                            "type": "Column",
                            "width": 65,
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "text": network_name,
                                    "color": "Light"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": sensor_name,
                                    "color": "Light",
                                    "weight": "Lighter",
                                    "spacing": "Small"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": model_name,
                                    "weight": "Lighter",
                                    "color": "Light",
                                    "spacing": "Small"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": timestamp,
                                    "weight": "Lighter",
                                    "color": "Light",
                                    "spacing": "Small"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": f'{elapsed_time} seconds',
                                    "weight": "Lighter",
                                    "color": "Light",
                                    "spacing": "Small"
                                }
                            ]
                        }
                    ],
                    "spacing": "Padding",
                    "horizontalAlignment": "Center"
                },
                {
                    "type": "ColumnSet",
                    "columns": [
                        {
                            "type": "Column",
                            "width": "auto",
                            "items": [
                                {
                                    "type": "Image",
                                    "altText": "",
                                    "url": "https://developer.webex.com/images/link-icon.png",
                                    "size": "Small",
                                    "width": "30px"
                                }
                            ],
                            "spacing": "Small"
                        },
                        {
                            "type": "Column",
                            "width": "auto",
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "text": f'["Go to Sensor Dashboard Link"]({sensor_link})',
                                    "horizontalAlignment": "Left",
                                    "size": "Medium"
                                }
                            ],
                            "verticalContentAlignment": "Center",
                            "horizontalAlignment": "Left",
                            "spacing": "Small"
                        }
                    ]
                }
            ]
        }
    }

    return card