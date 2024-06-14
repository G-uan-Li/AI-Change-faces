import multiprocessing
import gradio

from facefusion.uis.components import about, frame_processors, frame_processors_options, execution, execution_thread_count, execution_queue_count, memory, temp_frame, output_options, common_options, source, target, output, preview, trim_frame, face_analyser, face_selector, face_masker


def pre_check() -> bool:
	return True


def pre_render() -> bool:
	return True


def render() -> gradio.Blocks:
	with gradio.Blocks() as layout:
		with gradio.Row():
			with gradio.Column(scale = 2):
				with gradio.Blocks():
					about.render()
				with gradio.Blocks():
					frame_processors.render()
				with gradio.Blocks():
					frame_processors_options.render()
				with gradio.Blocks():
					execution.render()
					execution_thread_count.render()
					execution_queue_count.render()
				with gradio.Blocks():
					memory.render()
				with gradio.Blocks():
					temp_frame.render()
				with gradio.Blocks():
					output_options.render()
			with gradio.Column(scale = 2):
				with gradio.Blocks():
					source.render()
				with gradio.Blocks():
					target.render()
				with gradio.Blocks():
					output.render()
			with gradio.Column(scale = 3):
				with gradio.Blocks():
					preview.render()
				with gradio.Blocks():
					trim_frame.render()
				with gradio.Blocks():
					face_selector.render()
				with gradio.Blocks():
					face_masker.render()
				with gradio.Blocks():
					face_analyser.render()
				with gradio.Blocks():
					common_options.render()
		with gradio.Row():
			with gradio.Column(scale=1):
				gradio.Text("镜像作者：Ccj0221 欢迎加入QQ群：837217096 github主页：https://github.com/Ccj0221", font_size=12, color="grey")
                
	return layout


def listen() -> None:
	frame_processors.listen()
	frame_processors_options.listen()
	execution.listen()
	execution_thread_count.listen()
	execution_queue_count.listen()
	memory.listen()
	temp_frame.listen()
	output_options.listen()
	source.listen()
	target.listen()
	output.listen()
	preview.listen()
	trim_frame.listen()
	face_selector.listen()
	face_masker.listen()
	face_analyser.listen()
	common_options.listen()


def run(ui: gradio.Blocks) -> None:
    concurrency_count = min(8, multiprocessing.cpu_count())
    # 禁用IPv6并设置端口为6006
    ui.queue(concurrency_count=concurrency_count).launch(
        server_name='0.0.0.0',  # 仅使用IPv4
        server_port=6006,  # 设置端口为6006
        show_api=False,
        quiet=True,
        share=True
    )

#FaceFusion 2.4.1 - 人脸融合
#作者：J_0221
#链接：https://www.codewithgpu.com/i/Ccj0221/facefusion_Zh/Facefusion
#来源：CodeWithGpu
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
