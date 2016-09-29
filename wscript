## -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-

import sys

def build(bld):
    obj = bld.create_ns3_program('simulator-main', ['node'])
    obj.source = [ 
        'simulator-main.cc',
        'ls-routing-protocol/ls-routing-protocol.cc',
        'ls-routing-protocol/ls-message.cc',
        'ls-routing-protocol/ls-routing-helper.cc',
        'dv-routing-protocol/dv-routing-protocol.cc',
        'dv-routing-protocol/dv-message.cc',
        'dv-routing-protocol/dv-routing-helper.cc',
        'test-app/test-app.cc',
        'test-app/test-app-message.cc',
        'test-app/test-app-helper.cc',
        'common/ping-request.cc',
        'common/gu-log.cc',
        'common/gu-routing-protocol.cc',
        'common/gu-application.cc',
        'common/test-result.cc',
        ]
    headers = bld.new_task_gen('ns3header')
    headers.module = 'cosc525'
    headers.source = [
      'ls-routing-protocol/ls-routing-protocol.h',
      'ls-routing-protocol/ls-routing-helper.h',
      'ls-routing-protocol/ls-message.h',
      'dv-routing-protocol/dv-routing-protocol.h',
      'dv-routing-protocol/dv-routing-helper.h',
      'dv-routing-protocol/dv-message.h',
      'test-app/test-app.h',
      'test-app/test-app-message.h',
      'test-app/test-app-helper.h',
      'common/ping-request.h',
      'common/gu-log.h',
      'common/gu-routing-protocol.h',
      'common/gu-application.h',
      'common/test-result.h',
      ]
