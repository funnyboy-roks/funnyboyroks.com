<script lang="ts">
	import P5 from 'p5-svelte';
	import type { Sketch } from 'p5-svelte';
	let ratio = 2;
	const sketch: Sketch = (p5) => {
		let a1 = 0;
		let a2 = 0;

		p5.setup = () => {
			p5.createCanvas(800, 800);
			p5.background(0);
		};

		p5.draw = () => {
			let r = p5.width * .48;
			let ax = p5.sin(a2) * r + p5.width / 2;
			let ay = p5.cos(a2) * r + p5.height / 2;

			let x = p5.sin(a1) * r + p5.width / 2;
			let y = p5.cos(a1) * r + p5.height / 2;

			p5.stroke(255);
			p5.strokeWeight(1);
			p5.line(ax, ay, x, y);
			p5.strokeWeight(8);
			p5.point(ax, ay);
			p5.point(x, y);

			let speed = p5.PI / 128;

			a1 += speed;
			a2 += speed * ratio;
		};
	};
</script>

<div>
	<div class="sketch">
		<P5 {sketch} />
		<div class="input">
			<label for="ratio">Ratio: {ratio}</label>
			<input type="range" name="ratio" min="1" max="10" bind:value={ratio}>
		</div>
	</div>

	<div class="info">
		This is a simple sketch that has a cardiod that can be adjusted by the slider.
		The ratio is a multiplier for the speed of the second point going around the circle,
		meaning that if the ratio is 2, then the second point is moving twice as fast as the first
	</div>

</div>

<style>
	.sketch {
		display: flex;
		flex-direction: column;
		align-items: center;
		text-align: center;
	}

	.info {
		padding-top: 3rem;
		font-size: 1.5rem;
		font-family: 'Anonymous Pro';
	}
</style>
