# Copyright (c) 2009 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'variables': {
    'chromium_code': 1,
  },
  'includes': [
    '../build/branding.gypi',
    '../build/common.gypi',
    '../build/version.gypi',
  ],
  'target_defaults': {
    'include_dirs': [
      # The internal dir is first so that headers in internal can replace those
      # in external
      '../../<(internaldir)',
      '..',
      '../..',
      '../../<(gtestdir)',
      '../../<(nacldir)',
    ],
    'defines': [
      'O3D_PLUGIN_VERSION="<(plugin_version)"',
      'O3D_PLUGIN_EXTRAS_DIRECTORY="<(plugin_extras_directory)"',
    ],
    'conditions': [
      ['OS == "win"',
        {
          'msvs_settings': {
            'VCCLCompilerTool': {
              'ForcedIncludeFiles':
              'core/cross/precompile.h',
            },
          },
        },
      ],
      ['renderer == "d3d9" and OS == "win"',
        {
          'msvs_system_include_dirs': [
            '$(DXSDK_DIR)/Include',
          ],
        }
      ],
      ['OS == "linux"',
        {
          'cflags': [
            '-include',
            'core/cross/precompile.h',
          ],
        },
      ],
      ['renderer == "gl"',
        {
          'include_dirs': [
            '../../<(glewdir)/include',
            '../../<(cgdir)/include',
          ],
        },
      ],
      ['renderer == "gles2"',
        {
          'include_dirs': [
            '../../<(glewdir)/include',
          ],
        },
      ],
      ['disable_fbo == 1', {
        'defines': [
          'DISABLE_FBO',
        ],
      }],
    ],
  },
  'targets': [
    {
      'target_name': 'o3dCore',
      'type': 'static_library',
      'dependencies': [
        '../../<(jpegdir)/libjpeg.gyp:libjpeg',
        '../../<(pngdir)/libpng.gyp:libpng',
        '../../<(zlibdir)/zlib.gyp:zlib',
        '../../skia/skia.gyp:skia',
        '../third_party/glu/libtess.gyp:libtess',
      ],
      'sources': [
        'cross/bitmap.cc',
        'cross/bitmap.h',
        'cross/bitmap_dds.cc',
        'cross/bitmap_jpg.cc',
        'cross/bitmap_png.cc',
        'cross/bitmap_tga.cc',
        'cross/bounding_box.cc',
        'cross/bounding_box.h',
        'cross/buffer.cc',
        'cross/buffer.h',
        'cross/callback.h',
        'cross/canvas.cc',
        'cross/canvas.h',
        'cross/canvas_paint.cc',
        'cross/canvas_paint.h',
        'cross/canvas_shader.cc',
        'cross/canvas_shader.h',
        'cross/canvas_utils.h',
        'cross/class_manager.cc',
        'cross/class_manager.h',
        'cross/clear_buffer.cc',
        'cross/clear_buffer.h',
        'cross/client.cc',
        'cross/client.h',
        'cross/client_info.cc',
        'cross/client_info.h',
        'cross/core_metrics.cc',
        'cross/core_metrics.h',
        'cross/counter.cc',
        'cross/counter.h',
        'cross/counter_manager.cc',
        'cross/counter_manager.h',
        'cross/cursor.h',
        'cross/curve.cc',
        'cross/curve.h',
        'cross/ddsurfacedesc.h',
        'cross/display_mode.h',
        'cross/display_window.h',
        'cross/draw_context.cc',
        'cross/draw_context.h',
        'cross/draw_element.cc',
        'cross/draw_element.h',
        'cross/draw_list.cc',
        'cross/draw_list.h',
        'cross/draw_list_manager.cc',
        'cross/draw_list_manager.h',
        'cross/draw_pass.cc',
        'cross/draw_pass.h',
        'cross/effect.cc',
        'cross/effect.h',
        'cross/element.cc',
        'cross/element.h',
        'cross/error.h',
        'cross/error_status.cc',
        'cross/error_status.h',
        'cross/error_stream_manager.cc',
        'cross/error_stream_manager.h',
        'cross/evaluation_counter.cc',
        'cross/evaluation_counter.h',
        'cross/event.cc',
        'cross/event.h',
        'cross/event_callback.h',
        'cross/event_manager.cc',
        'cross/event_manager.h',
        'cross/fake_vertex_source.cc',
        'cross/fake_vertex_source.h',
        'cross/features.cc',
        'cross/features.h',
        'cross/field.cc',
        'cross/field.h',
        'cross/file_request.cc',
        'cross/file_request.h',
        'cross/float_n.h',
        'cross/function.cc',
        'cross/function.h',
        'cross/iclass_manager.cc',
        'cross/iclass_manager.h',
        'cross/id_manager.cc',
        'cross/id_manager.h',
        'cross/ierror_status.cc',
        'cross/ierror_status.h',
        'cross/image_utils.cc',
        'cross/imain_thread_task_poster.cc',
        'cross/imain_thread_task_poster.h',
        'cross/install_check.h',
        'cross/lost_resource_callback.h',
        'cross/material.cc',
        'cross/material.h',
        'cross/math_types.h',
        'cross/math_utilities.cc',
        'cross/math_utilities.h',
        'cross/matrix4_axis_rotation.cc',
        'cross/matrix4_axis_rotation.h',
        'cross/matrix4_composition.cc',
        'cross/matrix4_composition.h',
        'cross/matrix4_scale.cc',
        'cross/matrix4_scale.h',
        'cross/matrix4_translation.cc',
        'cross/matrix4_translation.h',
        'cross/message_commands.cc',
        'cross/message_commands.h',
        'cross/message_queue.cc',
        'cross/message_queue.h',
        'cross/named_object.cc',
        'cross/named_object.h',
        'cross/object_base.cc',
        'cross/object_base.h',
        'cross/object_manager.cc',
        'cross/object_manager.h',
        'cross/pack.cc',
        'cross/pack.h',
        'cross/param.cc',
        'cross/param.h',
        'cross/param_array.cc',
        'cross/param_array.h',
        'cross/param_cache.cc',
        'cross/param_cache.h',
        'cross/param_object.cc',
        'cross/param_object.h',
        'cross/param_operation.cc',
        'cross/param_operation.h',
        'cross/performance_timer.h',
        'cross/precompile.cc',
        'cross/precompile.h',
        'cross/primitive.cc',
        'cross/primitive.h',
        'cross/processed_path.cc',
        'cross/processed_path.h',
        'cross/profiler.cc',
        'cross/profiler.h',
        'cross/ray_intersection_info.cc',
        'cross/ray_intersection_info.h',
        'cross/render_context.cc',
        'cross/render_context.h',
        'cross/render_event.h',
        'cross/render_node.cc',
        'cross/render_node.h',
        'cross/render_surface.cc',
        'cross/render_surface.h',
        'cross/render_surface_set.cc',
        'cross/render_surface_set.h',
        'cross/renderer.cc',
        'cross/renderer.h',
        'cross/renderer_platform.h',
        'cross/sampler.cc',
        'cross/sampler.h',
        'cross/semantic_manager.cc',
        'cross/semantic_manager.h',
        'cross/service_dependency.h',
        'cross/service_implementation.h',
        'cross/service_interface_traits.h',
        'cross/service_locator.cc',
        'cross/service_locator.h',
        'cross/shape.cc',
        'cross/shape.h',
        'cross/skin.cc',
        'cross/skin.h',
        'cross/smart_ptr.h',
        'cross/standard_param.cc',
        'cross/standard_param.h',
        'cross/state.cc',
        'cross/state.h',
        'cross/state_set.cc',
        'cross/state_set.h',
        'cross/stream.cc',
        'cross/stream.h',
        'cross/stream_bank.cc',
        'cross/stream_bank.h',
        'cross/texture.cc',
        'cross/texture.h',
        'cross/texture_base.cc',
        'cross/texture_base.h',
        'cross/tick_event.h',
        'cross/timer.cc',
        'cross/timer.h',
        'cross/timingtable.h',
        'cross/transform.cc',
        'cross/transform.h',
        'cross/transformation_context.cc',
        'cross/transformation_context.h',
        'cross/tree_traversal.cc',
        'cross/tree_traversal.h',
        'cross/types.h',
        'cross/vector_map.h',
        'cross/vertex_source.cc',
        'cross/vertex_source.h',
        'cross/viewport.cc',
        'cross/viewport.h',
        'cross/visitor_base.h',
        'cross/weak_ptr.h',
        'cross/gpu2d/arena.h',
        'cross/gpu2d/cubic_classifier.cc',
        'cross/gpu2d/cubic_classifier.h',
        'cross/gpu2d/cubic_math_utils.cc',
        'cross/gpu2d/cubic_math_utils.h',
        'cross/gpu2d/cubic_texture_coords.cc',
        'cross/gpu2d/cubic_texture_coords.h',
        'cross/gpu2d/interval_tree.h',
        'cross/gpu2d/local_triangulator.cc',
        'cross/gpu2d/local_triangulator.h',
        'cross/gpu2d/path_cache.cc',
        'cross/gpu2d/path_cache.h',
        'cross/gpu2d/path_processor.cc',
        'cross/gpu2d/path_processor.h',
        'cross/gpu2d/red_black_tree.h',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '..',
        ],
      },
      'conditions': [
        ['OS == "win"',
          {
            'sources': [
              'win/display_window_win.h',
              'win/performance_timer.cc',
            ],
            'direct_dependent_settings': {
              'include_dirs': [
                'win',
              ],
            },
          },
        ],
        ['renderer == "gl"',
          {
            'dependencies': [
              '../build/libs.gyp:cg_libs',
              '../build/libs.gyp:gl_libs',
            ],
          },
        ],
        ['renderer == "gles2"',
          {
            'dependencies': [
              '../build/libs.gyp:gles2_libs',
            ],
          },
        ],
        ['OS == "linux"',
          {
            'sources': [
              'linux/display_window_linux.h',
              'linux/performance_timer.cc',
            ],
            'direct_dependent_settings': {
              'include_dirs': [
                'linux',
              ],
            },
          },
        ],
        ['OS == "mac"',
          {
            'sources': [
              'mac/display_window_mac.h',
              'mac/performance_timer.cc',
            ],
            'direct_dependent_settings': {
              'include_dirs': [
                'mac',
              ],
            },
            'xcode_settings': {
              'GCC_PREFIX_HEADER': 'cross/precompile.h',
              'GCC_PFE_FILE_C_DIALECTS': 'c++',
            },
          },
        ],
      ],
    },
    {
      'target_name': 'o3dCorePlatform',
      'type': 'static_library',
      'dependencies': [
        '../../skia/skia.gyp:skia',
      ],
      'sources': [
      ],
      'conditions': [
        ['OS == "mac"',
          {
            'xcode_settings': {
              'GCC_PREFIX_HEADER': 'cross/precompile.h',
              'GCC_PFE_FILE_C_DIALECTS': 'c++',
            },
          },
        ],
        ['renderer == "gl"',
          {
            'sources': [
              'cross/gl/buffer_gl.cc',
              'cross/gl/buffer_gl.h',
              'cross/gl/draw_element_gl.cc',
              'cross/gl/draw_element_gl.h',
              'cross/gl/effect_gl.cc',
              'cross/gl/effect_gl.h',
              'cross/gl/install_check.cc',
              'cross/gl/param_cache_gl.cc',
              'cross/gl/param_cache_gl.h',
              'cross/gl/primitive_gl.cc',
              'cross/gl/primitive_gl.h',
              'cross/gl/render_surface_gl.cc',
              'cross/gl/render_surface_gl.h',
              'cross/gl/renderer_gl.cc',
              'cross/gl/renderer_gl.h',
              'cross/gl/sampler_gl.cc',
              'cross/gl/sampler_gl.h',
              'cross/gl/stream_bank_gl.cc',
              'cross/gl/stream_bank_gl.h',
              'cross/gl/texture_gl.cc',
              'cross/gl/texture_gl.h',
              'cross/gl/utils_gl-inl.h',
              'cross/gl/utils_gl.cc',
              'cross/gl/utils_gl.h',
            ],
            'dependencies': [
              '../build/libs.gyp:gl_libs',
            ],
          },
        ],
        ['renderer == "gles2"',
          {
            'sources': [
              'cross/gles2/buffer_gles2.cc',
              'cross/gles2/buffer_gles2.h',
              'cross/gles2/draw_element_gles2.cc',
              'cross/gles2/draw_element_gles2.h',
              'cross/gles2/effect_gles2.cc',
              'cross/gles2/effect_gles2.h',
              'cross/gles2/install_check.cc',
              'cross/gles2/param_cache_gles2.cc',
              'cross/gles2/param_cache_gles2.h',
              'cross/gles2/primitive_gles2.cc',
              'cross/gles2/primitive_gles2.h',
              'cross/gles2/render_surface_gles2.cc',
              'cross/gles2/render_surface_gles2.h',
              'cross/gles2/renderer_gles2.cc',
              'cross/gles2/renderer_gles2.h',
              'cross/gles2/sampler_gles2.cc',
              'cross/gles2/sampler_gles2.h',
              'cross/gles2/stream_bank_gles2.cc',
              'cross/gles2/stream_bank_gles2.h',
              'cross/gles2/texture_gles2.cc',
              'cross/gles2/texture_gles2.h',
              'cross/gles2/utils_gles2-inl.h',
              'cross/gles2/utils_gles2.cc',
              'cross/gles2/utils_gles2.h',
            ],
            'dependencies': [
              '../build/libs.gyp:gles2_libs',
            ],
          },
        ],
        ['renderer == "d3d9" and OS == "win"',
          {
            'sources': [
              'win/d3d9/buffer_d3d9.cc',
              'win/d3d9/buffer_d3d9.h',
              'win/d3d9/d3d_entry_points.h',
              'win/d3d9/draw_element_d3d9.cc',
              'win/d3d9/draw_element_d3d9.h',
              'win/d3d9/effect_d3d9.cc',
              'win/d3d9/effect_d3d9.h',
              'win/d3d9/install_check.cc',
              'win/d3d9/param_cache_d3d9.cc',
              'win/d3d9/param_cache_d3d9.h',
              'win/d3d9/primitive_d3d9.cc',
              'win/d3d9/primitive_d3d9.h',
              'win/d3d9/render_surface_d3d9.cc',
              'win/d3d9/render_surface_d3d9.h',
              'win/d3d9/renderer_d3d9.cc',
              'win/d3d9/renderer_d3d9.h',
              'win/d3d9/sampler_d3d9.cc',
              'win/d3d9/sampler_d3d9.h',
              'win/d3d9/stream_bank_d3d9.cc',
              'win/d3d9/stream_bank_d3d9.h',
              'win/d3d9/texture_d3d9.cc',
              'win/d3d9/texture_d3d9.h',
              'win/d3d9/utils_d3d9.cc',
              'win/d3d9/utils_d3d9.h',
            ],
          },
        ],
        ['renderer == "cairo"',
          {
            'sources': [
              'cross/cairo/install_check.cc',
              'cross/cairo/layer.cc',
              'cross/cairo/layer.h',
              'cross/cairo/renderer_cairo.cc',
              'cross/cairo/renderer_cairo.h',
              'cross/cairo/texture_cairo.cc',
              'cross/cairo/texture_cairo.h',
            ],
            'dependencies': [
              '../build/libs.gyp:cairo_libs',
            ],
          },
        ],
      ],
    },
    {
      'target_name': 'o3dCoreTest',
      'type': 'none',
      'direct_dependent_settings': {
        'sources': [
          'cross/bitmap_test.cc',
          'cross/bounding_box_test.cc',
          'cross/buffer_test.cc',
          'cross/class_manager_test.cc',
          'cross/client_test.cc',
          'cross/counter_test.cc',
          'cross/curve_test.cc',
          'cross/draw_element_test.cc',
          'cross/draw_list_test.cc',
          'cross/draw_pass_test.cc',
          'cross/effect_test.cc',
          'cross/element_test.cc',
          'cross/event_manager_test.cc',
          'cross/features_test.cc',
          'cross/field_test.cc',
          'cross/float_n_test.cc',
          'cross/function_test.cc',
          'cross/image_utils_test.cc',
          'cross/material_test.cc',
          'cross/math_utilities_test.cc',
          'cross/matrix4_axis_rotation_test.cc',
          'cross/matrix4_composition_test.cc',
          'cross/matrix4_scale_test.cc',
          'cross/matrix4_translation_test.cc',
          'cross/message_commands_test.cc',
          'cross/message_queue_test.cc',
          'cross/object_base_test.cc',
          'cross/pack_test.cc',
          'cross/param_array_test.cc',
          'cross/param_object_test.cc',
          'cross/param_operation_test.cc',
          'cross/param_test.cc',
          'cross/performance_timer_test.cc',
          'cross/primitive_test.cc',
          'cross/ray_intersection_info_test.cc',
          'cross/render_node_test.cc',
          'cross/renderer_test.cc',
          'cross/service_locator_test.cc',
          'cross/shape_test.cc',
          'cross/skin_test.cc',
          'cross/smart_ptr_test.cc',
          'cross/state_set_test.cc',
          'cross/state_test.cc',
          'cross/stream_bank_test.cc',
          'cross/stream_test.cc',
          'cross/texture_base_test.cc',
          'cross/texture_test.cc',
          'cross/transform_test.cc',
          'cross/tree_traversal_test.cc',
          'cross/vector_map_test.cc',
          'cross/vertex_source_test.cc',
          'cross/visitor_base_test.cc',
          'cross/weak_ptr_test.cc',
          'cross/gpu2d/arena_test.cc',
          'cross/gpu2d/cubic_classifier_test.cc',
          'cross/gpu2d/interval_tree_test.cc',
          'cross/gpu2d/local_triangulator_test.cc',
          'cross/gpu2d/red_black_tree_test.cc',
          'cross/gpu2d/tree_test_helpers.cc',
          'cross/gpu2d/tree_test_helpers.h',
        ],
      },
    },
  ],
}

# Local Variables:
# tab-width:2
# indent-tabs-mode:nil
# End:
# vim: set expandtab tabstop=2 shiftwidth=2:
