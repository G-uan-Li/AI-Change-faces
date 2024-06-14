from typing import Any, Dict, Optional

WORDING : Dict[str, Any] =\
{
    'conda_not_activated': 'Conda未激活',
    'python_not_supported': '不支持该Python版本，请升级到{version}或更高版本',
    'ffmpeg_not_installed': 'FFMpeg未安装',
    'creating_temp': '正在创建临时资源',
    'extracting_frames': '正在以{resolution}的分辨率和每秒{fps}帧的速度提取帧',
    'extracting_frames_succeed': '提取帧成功',
    'extracting_frames_failed': '提取帧失败',
    'analysing': '正在分析',
    'processing': '正在处理',
    'downloading': '正在下载',
    'temp_frames_not_found': '未找到临时帧',
    'copying_image': '正在复制分辨率为{resolution}的图像',
    'copying_image_succeed': '复制图像成功',
    'copying_image_failed': '复制图像失败',
    'finalizing_image': '正在完成分辨率为{resolution}的图像',
    'finalizing_image_succeed': '完成图像成功',
    'finalizing_image_skipped': '跳过完成图像',
    'merging_video': '正在以{resolution}的分辨率和每秒{fps}帧的速度合并视频',
    'merging_video_succeed': '合并视频成功',
    'merging_video_failed': '合并视频失败',
    'skipping_audio': '跳过音频',
    'restoring_audio_succeed': '恢复音频成功',
    'restoring_audio_skipped': '跳过恢复音频',
    'clearing_temp': '正在清理临时资源',
    'processing_stopped': '处理已停止',
    'processing_image_succeed': '处理为图像成功，用时{seconds}秒',
    'processing_image_failed': '处理为图像失败',
    'processing_video_succeed': '处理为视频成功，用时{seconds}秒',
    'processing_video_failed': '处理为视频失败',
    'model_download_not_done': '模型下载未完成',
    'model_file_not_present': '模型文件不存在',
    'select_image_source': '选择图像源路径',
    'select_audio_source': '选择音频源路径',
    'select_video_target': '选择视频目标路径',
    'select_image_or_video_target': '选择图像或视频目标路径',
    'select_file_or_directory_output': '选择文件或目录输出路径',
    'no_source_face_detected': '未检测到源人脸',
    'frame_processor_not_loaded': '无法加载帧处理器{frame_processor}',
    'frame_processor_not_implemented': '帧处理器{frame_processor}未正确实现',
    'ui_layout_not_loaded': '无法加载UI布局{ui_layout}',
    'ui_layout_not_implemented': 'UI布局{ui_layout}未正确实现',
    'stream_not_loaded': '无法加载流{stream_mode}',
    'point': '。',
    'comma': '，',
    'colon': '：',
    'question_mark': '？',
    'exclamation_mark': '！',
    'help':
	{
		# installer
		'install_dependency': '选择要安装的{dependency}变体',
		'skip_conda': '跳过Conda环境检查',
		# general
		'source': '选择单个或多个源图像或音频',
		'target': '选择单个目标图像或视频',
		'output': '指定输出文件或目录',
		# misc
		'force_download': '强制自动下载并退出',
		'skip_download': '省略自动下载和远程查找',
		'headless': '在没有用户界面的情况下运行程序',
		'log_level': '调整终端显示的消息的等级',
		# execution
		'execution_providers': '使用不同的提供者加速模型推理（选择：{choices}，...）',
		'execution_thread_count': '指定处理时的并行线程数',
		'execution_queue_count': '指定每个线程处理的帧数',
		# memory
		'video_memory_strategy': '平衡快速帧处理和低VRAM使用',
		'system_memory_limit': '限制处理时可用的RAM',
		# face analyser
		'face_analyser_order': '指定人脸分析器检测人脸的顺序',
		'face_analyser_age': '根据年龄过滤检测到的人脸',
		'face_analyser_gender': '根据性别过滤检测到的人脸',
		'face_detector_model': '选择负责检测人脸的模型',
		'face_detector_size': '指定提供给人脸检测器的帧大小',
		'face_detector_score': '根据置信分数过滤检测到的人脸',
		'face_landmarker_score': '根据置信分数过滤检测到的源',
		# face selector
		'face_selector_mode': '使用基于参考的跟踪或简单匹配',
		'reference_face_position': '指定用于创建参考人脸的位置',
		'reference_face_distance': '指定参考人脸与目标人脸之间的期望相似度',
		'reference_frame_number': '指定用于创建参考人脸的帧',
		# face mask
		'face_mask_types': '混合和匹配不同的面部遮罩类型（选择：{choices}）',
		'face_mask_blur': '指定应用于方框遮罩的模糊程度',
		'face_mask_padding': '为方框遮罩应用顶部、右侧、底部和左侧的填充',
		'face_mask_regions': '选择用于区域遮罩的面部特征（选择：{choices}）',
		# frame extraction
		'trim_frame_start': '指定目标视频的开始帧',
		'trim_frame_end': '指定目标视频的结束帧',
		'temp_frame_format': '指定临时资源的格式',
		'keep_temp': '处理后保留临时资源',
		# output creation
		'output_image_quality': '指定图像质量',
		'output_image_resolution': '根据目标图像指定图像输出分辨率',
		'output_video_encoder': '视频压缩的编码器',
		'output_video_preset': '平衡快速视频处理和视频文件大小',
		'output_video_quality': '视频质量',
		'output_video_resolution': '视频输出分辨率',
		'output_video_fps': '视频输出帧率',
		'skip_audio': '省略视频中的音频',
		# frame processors
		'frame_processors': '加载单个或多个帧处理器。 （选择：{choices}，...）',
		'face_debugger_items': '加载单个或多个帧处理器（选择：{choices}）',
		'face_enhancer_model': '选择负责增强人脸的模型',
		'face_enhancer_blend': '将增强效果与之前的人脸融合',
		'face_swapper_model': '选择负责交换人脸的模型',
		'frame_colorizer_model': '选择负责为帧着色的模型',
		'frame_colorizer_blend': '将着色效果与之前的帧融合',
		'frame_enhancer_model': '选择负责增强帧的模型',
		'frame_enhancer_blend': '将增强效果与之前的帧融合',
		'lip_syncer_model': '选择负责同步嘴唇的模型',
		# uis
		'ui_layouts': '启动单个或多个UI布局（选择：{choices}，...）'
	},
	'uis':
	{
		# general
		'start_button': '开始',
		'stop_button': '停止',
		'clear_button': '清除缓存',
		# about
		'donate_button': '社区指南',
		# benchmark
		'benchmark_results_dataframe': '基准测试结果',
		# benchmark options
		'benchmark_runs_checkbox_group': '基准测试运行次数',
		'benchmark_cycles_slider': '基准测试周期',
		# common options
		'common_options_checkbox_group': '通用选项',
		# execution
		'execution_providers_checkbox_group': '执行程序',
		# execution queue count
		'execution_queue_count_slider': '执行队列数量',
		# execution thread count
		'execution_thread_count_slider': '执行线程数量',
		# face analyser
		'face_analyser_order_dropdown': '人脸分析器顺序',
		'face_analyser_age_dropdown': '人脸分析器年龄',
		'face_analyser_gender_dropdown': '人脸分析器性别',
		'face_detector_model_dropdown': '人脸检测器模型',
		'face_detector_size_dropdown': '人脸检测器大小',
		'face_detector_score_slider': '人脸检测器置信度',
		'face_landmarker_score_slider': '人脸地标置信度',
		# face masker
		'face_mask_types_checkbox_group': '面部遮罩类型',
		'face_mask_blur_slider': '面部遮罩模糊度',
		'face_mask_padding_top_slider': '顶部填充',
		'face_mask_padding_right_slider': '右侧填充',
		'face_mask_padding_bottom_slider': '底部填充',
		'face_mask_padding_left_slider': '左侧填充',
		'face_mask_region_checkbox_group': '面部遮罩区域',
		# face selector
		'face_selector_mode_dropdown': '人脸选择器模式',
		'reference_face_gallery': '参考人脸',
		'reference_face_distance_slider': '参考人脸与目标人脸距离',
		# frame processors
		'frame_processors_checkbox_group': '帧处理器',
		# frame processors options
		'face_debugger_items_checkbox_group': '人脸调试器项目',
		'face_enhancer_model_dropdown': '人脸增强器模型',
		'face_enhancer_blend_slider': '人脸增强器混合',
		'face_swapper_model_dropdown': '人脸交换器模型',
		'frame_colorizer_model_dropdown': '帧着色器模型',
		'frame_colorizer_blend_slider': '帧着色器混合',
		'frame_enhancer_model_dropdown': '帧增强器模型',
		'frame_enhancer_blend_slider': '帧增强器混合',
		'lip_syncer_model_dropdown': '嘴唇同步器模型',
		# memory
		'video_memory_strategy_dropdown': '视频内存策略',
		'system_memory_limit_slider': '系统内存限制',
		# output
		'output_image_or_video': '输出',
		# output options
		'output_path_textbox': '输出路径',
		'output_image_quality_slider': '输出图像质量',
		'output_image_resolution_dropdown': '输出图像分辨率',
		'output_video_encoder_dropdown': '输出视频编码器',
		'output_video_preset_dropdown': '输出视频预设',
		'output_video_quality_slider': '输出视频质量',
		'output_video_resolution_dropdown': '输出视频分辨率',
		'output_video_fps_slider': '输出视频帧率',
		# preview
		'preview_image': '预览',
		'preview_frame_slider': '预览帧',
		# source
		'source_file': '参考人脸图片',
		# target
		'target_file': '需要替换的人脸（图片/视频）',
		# temp frame
		'temp_frame_format_dropdown': '临时帧格式',
		# trim frame
		'trim_frame_start_slider': '裁剪起始帧',
		'trim_frame_end_slider': '裁剪结束帧',
		# webcam
		'webcam_image': '摄像头',
		# webcam options
		'webcam_mode_radio': '摄像头模式',
		'webcam_resolution_dropdown': '摄像头分辨率',
		'webcam_fps_slider': '摄像头帧率'
	}
}


def get(key : str) -> Optional[str]:
	if '.' in key:
		section, name = key.split('.')
		if section in WORDING and name in WORDING[section]:
			return WORDING[section][name]
	if key in WORDING:
		return WORDING[key]
	return None
