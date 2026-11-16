"""Generates the static site pages from shared header/footer templates."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

TABS = [
    ("Home", "index.html", "home"),
    ("Projects", "projects/index.html", "projects"),
    ("About", "about.html", "about"),
    ("Resume & Contact", "contact.html", "contact"),
]


def page(path, title, active, body, desc):
    depth = path.count("/")
    pre = "../" * depth
    nav = "\n".join(
        f'<li><a href="{pre}{href}"{" aria-current=\"page\"" if key == active else ""}>{label}</a></li>'
        for label, href, key in TABS
    )
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Arnav Tevatia</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="{pre}assets/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to main content</a>
<header class="site">
  <div class="bar">
    <a class="brand" href="{pre}index.html">Arnav Tevatia<span>.</span></a>
    <nav class="tabs" aria-label="Main">
      <ul>
{nav}
      </ul>
    </nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site">
  <div class="bar">
    <span>Arnav Tevatia, Cornell Engineering, Class of 2027</span>
    <span><a href="https://www.linkedin.com/in/arnav-tevatia">LinkedIn</a> · <a href="https://github.com/arnavtevatia">GitHub</a></span>
  </div>
</footer>
</body>
</html>
"""
    out = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)


# ---------------- Home ----------------
HOME = """
<section class="hero">
  <div>
    <p class="eyebrow">Robotics and physical AI engineer · Division I squash captain</p>
    <h1>I make models run fast and work on real machines.</h1>
    <p class="lede">I'm a Cornell computer science senior focused on machine learning systems. I've written GPU code from scratch, trained language models with a fraction of the usual parameters, and worked on teleoperation software for real robots. I'm looking for a full-time engineering role on a small robotics team, starting as early as January 2027.</p>
    <p class="lede">On the squash court and in the lab I run the same loop: try something, measure what happened, adjust. <a href="about.html">See how that carries over</a>.</p>
    <a class="btn" href="projects/index.html">See my projects</a>
    <a class="btn ghost" href="about.html">How I work</a>
  </div>
  <aside class="hero-card" aria-label="Quick facts">
    <h2>At a glance</h2>
    <ul>
      <li>B.S. Computer Science, ML concentration, Cornell 2027</li>
      <li>Robotics internship: teleoperation and force feedback (summer 2026)</li>
      <li>Captain, Cornell Division I Men's Squash</li>
      <li>Team USA gold medalist, 2022 Pan American Junior Games</li>
    </ul>
  </aside>
</section>

<h2>Featured work</h2>
<div class="grid">
  <a class="card" href="projects/teleoperation.html">
    <span><span class="tag">Real robots</span><span class="tag">Internship</span></span>
    <h3>Force feedback for robot teleoperation</h3>
    <p class="muted">Letting a human operator feel what a robot touches, without adding a force sensor.</p>
    <span class="more">Read the project →</span>
  </a>
  <a class="card" href="projects/cuda-kernels.html">
    <span><span class="tag">Speed</span><span class="tag">GPU code</span></span>
    <div class="stat">2.5 s → 0.05 s</div>
    <h3>GPU kernels for transformer inference</h3>
    <p class="muted">The same math, rewritten four times until it ran about 50 times faster.</p>
    <span class="more">See the results →</span>
  </a>
  <a class="card" href="projects/lora-dora.html">
    <span><span class="tag">AI training</span><span class="tag">Efficiency</span></span>
    <div class="stat">843× fewer</div>
    <h3>Fine-tuning GPT-2 with LoRA and DoRA</h3>
    <p class="muted">Training an add-on 843 times smaller than the model, and getting a better result.</p>
    <span class="more">See the results →</span>
  </a>
  <a class="card" href="projects/gan-demo.html">
    <span><span class="tag">Interactive</span><span class="tag">Teaching</span></span>
    <h3>Why GANs use a different loss</h3>
    <p class="muted">An interactive explainer you can play with right on the page.</p>
    <span class="more">Try the demo →</span>
  </a>
</div>
"""

# ---------------- Projects index ----------------
PROJECTS = """
<p class="eyebrow">Projects</p>
<h1>Work you can check</h1>
<p class="lede">Each project has its own page with the problem, what I built, the results with a plain-language explanation, and the code itself.</p>
<div class="grid">
  <a class="card" href="teleoperation.html">
    <span><span class="tag">Robotics startup</span><span class="tag">Summer 2026</span></span>
    <h3>Force feedback for robot teleoperation</h3>
    <p class="muted">Estimating contact force without a dedicated sensor, and running control code in a real-time system.</p>
    <span class="more">Open →</span>
  </a>
  <a class="card" href="cuda-kernels.html">
    <span><span class="tag">CS 4787</span><span class="tag">CUDA, C++</span></span>
    <h3>GPU kernels for transformer inference</h3>
    <p class="muted">From a naive kernel to shared-memory tiling to TensorCores, benchmarked against PyTorch.</p>
    <span class="more">Open →</span>
  </a>
  <a class="card" href="lora-dora.html">
    <span><span class="tag">CS 4782</span><span class="tag">PyTorch</span></span>
    <h3>LoRA and DoRA on GPT-2, from scratch</h3>
    <p class="muted">Parameter-efficient fine-tuning without any library, compared across six configurations.</p>
    <span class="more">Open →</span>
  </a>
  <a class="card" href="gan-demo.html">
    <span><span class="tag">Interactive</span><span class="tag">JavaScript</span></span>
    <h3>GAN loss curves demo</h3>
    <p class="muted">A six-step interactive explainer of why the non-saturating loss trains faster.</p>
    <span class="more">Open →</span>
  </a>
</div>
"""

# ---------------- Teleoperation ----------------
TELEOP = """
<p class="crumb"><a href="index.html">Projects</a> / Teleoperation</p>
<p class="eyebrow">Internship, robotics startup, summer 2026</p>
<h1>Force feedback for robot teleoperation</h1>
<p class="lede">When a person controls a robot arm remotely, they can't feel what the gripper is touching. My summer work was about giving that sense of touch back to the operator, and getting control code to run reliably on real hardware.</p>

<div class="plain">
  <strong>In plain language</strong>
  Imagine steering a robot hand with a controller. Without force feedback, you can crush an object or drop it because you have no idea how hard you are squeezing. Force feedback pushes back on your hand so you can feel the grip.
</div>

<h2>The problem</h2>
<p>Force sensors add cost, weight and wiring to a robot. I worked on estimating contact force from signals the robot already has, so the operator could get feedback without adding a dedicated sensor.</p>

<h2>What I worked on</h2>
<ul>
  <li>A force estimation system for teleoperation that needed no extra sensor.</li>
  <li>Control code deployed into the robot's real-time control system.</li>
  <li>Benchmarking vision-language-action (VLA) models on the team's tasks.</li>
</ul>

<h2>Why it matters to me</h2>
<p>This was the first time my code had to work on a physical machine instead of a benchmark. Bugs showed up as a robot doing the wrong thing, which made testing and measurement feel very different from coursework.</p>

<p class="muted small">The company is early stage, so I'm only sharing what I'm allowed to. I'll add a demo video and results here once they're cleared for public use.</p>
"""

# ---------------- CUDA ----------------
CUDA = r"""
<p class="crumb"><a href="index.html">Projects</a> / GPU kernels</p>
<p class="eyebrow">CS 4787, Cornell · CUDA, C++, PyTorch</p>
<h1>GPU kernels for transformer inference</h1>
<p class="lede">Most of the work a language model does when it answers a question is one operation: multiplying large matrices. I wrote that operation from scratch on a GPU four times, each version smarter than the last, and measured every step.</p>

<div class="stats">
  <div class="stat-box"><div class="num">2.5 s → 0.05 s</div><div class="lbl">Time for one 4096 × 4096 multiply, first version vs. TensorCore version</div></div>
  <div class="stat-box"><div class="num">~50–130×</div><div class="lbl">Speedup over my first version, depending on matrix size</div></div>
  <div class="stat-box"><div class="num">4</div><div class="lbl">Kernel designs, each benchmarked for speed and accuracy</div></div>
</div>

<div class="plain">
  <strong>What the numbers mean</strong>
  A task that took my first version about two and a half seconds took my final version about one twentieth of a second. For a chatbot, faster matrix multiplies mean faster answers and fewer GPUs to pay for. For a robot, it means the model can react in time.
</div>

<figure>
  <img src="../assets/cuda-benchmark.png" alt="Line chart on a log scale of runtime versus matrix size from 256 to 4096. The naive kernels (sgemm_p1, hgemm_p1) are slowest, reaching about 2.5 to 3.4 seconds at size 4096. Tiled kernels are several times faster. TensorCore kernels hgemm_p3 and hgemm_p4 are about 0.05 to 0.06 seconds at 4096. PyTorch's cuBLAS FP16 is fastest at about 0.003 seconds.">
  <figcaption>Runtime vs. matrix size (log scale, lower is faster). Each step down is a design change: tiling, then TensorCores. PyTorch (cuBLAS) is still fastest at large sizes, and I explain why below.</figcaption>
</figure>

<h2>Four versions, one idea each</h2>
<div class="table-wrap">
<table>
  <caption>Kernel designs</caption>
  <thead><tr><th>Version</th><th>Idea</th><th>Plain language</th></tr></thead>
  <tbody>
    <tr><td>1. Naive</td><td>One thread per output value, reading straight from global memory</td><td>Every worker walks to the warehouse for every single item.</td></tr>
    <tr><td>2. Tiled</td><td>Blocks of 256 threads share 16×16 tiles in fast on-chip memory</td><td>A team brings a box back to their desk once, then reuses it 16 times.</td></tr>
    <tr><td>3. TensorCore</td><td>WMMA instructions run the multiply on dedicated matrix hardware</td><td>Hand the job to a machine built for exactly this task.</td></tr>
    <tr><td>4. Mixed precision</td><td>Half-precision inputs, full-precision running sums</td><td>Same speed, but keep the running total exact so rounding errors don't pile up.</td></tr>
  </tbody>
</table>
</div>

<h2>Accuracy, not just speed</h2>
<p>Fast and wrong is useless, so I checked every kernel against a high-precision reference. Keeping the running sum in full precision (version 4) cut the error from about 1 in 70,000 to about 1 in 15 billion, at essentially the same speed. This is the same trade-off that makes mixed-precision training work in practice.</p>

<h2>What I'd do next</h2>
<p>NVIDIA's cuBLAS still wins at large sizes. The gap comes from techniques I left out on purpose: larger tiles with register blocking, staging TensorCore inputs in shared memory, double buffering to hide memory delays, avoiding shared-memory bank conflicts, and autotuning per GPU. Those are my next steps, roughly in order of expected payoff.</p>

<details>
  <summary>See the TensorCore kernel (CUDA)</summary>
<pre><code>__global__ void hgemm_p3_kernel(const __half* A, const __half* B, __half* C,
                                const size_t M, const size_t N, const size_t K) {
  // each block is a single warp that computes one 16x16 tile of C
  const int row = blockIdx.x * 16;
  const int col = blockIdx.y * 16;

  wmma::fragment&lt;wmma::matrix_a, 16, 16, 16, half, wmma::row_major&gt; a_frag;
  wmma::fragment&lt;wmma::matrix_b, 16, 16, 16, half, wmma::col_major&gt; b_frag;
  wmma::fragment&lt;wmma::accumulator, 16, 16, 16, half&gt; c_frag;
  wmma::fill_fragment(c_frag, __float2half(0.0f));

  for (int k0 = 0; k0 &lt; (int)K; k0 += 16) {
    const half* tile_A = reinterpret_cast&lt;const half*&gt;(A + row * K + k0);
    // read B (N x K, row-major) as B^T (K x N, col-major): no transpose needed
    const half* tile_B = reinterpret_cast&lt;const half*&gt;(B + col * K + k0);
    wmma::load_matrix_sync(a_frag, tile_A, K);
    wmma::load_matrix_sync(b_frag, tile_B, K);
    wmma::mma_sync(c_frag, a_frag, b_frag, c_frag);  // runs on TensorCores
  }
  // ... store c_frag to C
}</code></pre>
</details>

<p class="small muted">Full source and benchmark script: <a href="https://github.com/arnavtevatia/cuda-transformer-inference-optimization">github.com/arnavtevatia/cuda-transformer-inference-optimization</a></p>
"""

# ---------------- LoRA ----------------
LORA = """
<p class="crumb"><a href="index.html">Projects</a> / LoRA and DoRA</p>
<p class="eyebrow">CS 4782 Deep Learning, Cornell · PyTorch</p>
<h1>Fine-tuning GPT-2 with LoRA and DoRA, from scratch</h1>
<p class="lede">Adapting a language model to new text usually means retraining all of its 124 million settings. LoRA freezes the model and trains a tiny add-on instead. I implemented LoRA and its newer extension DoRA myself, with no fine-tuning library, and compared six setups.</p>

<div class="stats">
  <div class="stat-box"><div class="num">843×</div><div class="lbl">Fewer trainable parameters with LoRA r=4 (147K vs. 124M)</div></div>
  <div class="stat-box"><div class="num">32.13 → 25.65</div><div class="lbl">Perplexity, full fine-tuning vs. LoRA r=4 (lower is better)</div></div>
  <div class="stat-box"><div class="num">25.22</div><div class="lbl">Best perplexity, from my DoRA extension at r=8</div></div>
</div>

<div class="plain">
  <strong>What the numbers mean</strong>
  Perplexity measures how surprised a model is by new text. Lower means it predicts better. Training only a small add-on, 843 times smaller than the full model, gave a better result than retraining everything. That means cheaper training and a much smaller file to store for each new task.
</div>

<figure>
  <img src="../assets/lora-perplexity.png" alt="Bar chart of validation perplexity, lower is better. Frozen GPT-2 36.08, full fine-tune 32.13, LoRA r=4 25.65, LoRA r=8 25.26, DoRA r=4 25.50, DoRA r=8 25.22.">
  <figcaption>Validation perplexity on WikiText-2 for all six configurations.</figcaption>
</figure>

<div class="table-wrap">
<table>
  <caption>Results</caption>
  <thead><tr><th>Configuration</th><th>Trainable parameters</th><th>Perplexity</th><th>Peak GPU memory</th></tr></thead>
  <tbody>
    <tr><td>Frozen GPT-2</td><td>0</td><td>36.08</td><td>N/A</td></tr>
    <tr><td>Full fine-tune</td><td>124,440K</td><td>32.13</td><td>5,753 MB</td></tr>
    <tr class="hl"><td>LoRA r=4</td><td>147K</td><td>25.65</td><td>4,118 MB</td></tr>
    <tr><td>LoRA r=8</td><td>295K</td><td>25.26</td><td>4,120 MB</td></tr>
    <tr><td>DoRA r=4</td><td>166K</td><td>25.50</td><td>4,227 MB</td></tr>
    <tr class="hl"><td>DoRA r=8</td><td>313K</td><td>25.22</td><td>4,228 MB</td></tr>
  </tbody>
</table>
</div>

<h2>The surprise</h2>
<p>I expected LoRA to roughly match full fine-tuning, not beat it. The training curves explain why: full fine-tuning starts overfitting WikiText-2's small training set after the first epoch, while LoRA's small add-on can't memorize as much, so it generalizes better.</p>
<figure>
  <img src="../assets/lora-curves.png" alt="Line chart of validation perplexity over three epochs. Full fine-tuning gets worse, rising from about 27.8 to 32.1, while all four LoRA and DoRA setups keep improving, ending between 25.2 and 25.7.">
  <figcaption>Validation perplexity by epoch. Full fine-tuning gets worse after epoch 1 while the adapters keep improving.</figcaption>
</figure>

<h2>How I made sure it was right</h2>
<ul>
  <li><strong>Parameter audit:</strong> confirmed only the adapter weights could change during training.</li>
  <li><strong>Equivalence check:</strong> confirmed the adapted model's output matched the original GPT-2 exactly before training started.</li>
</ul>

<h2>What's next</h2>
<p>DoRA beat LoRA at the same size every time, but by less than the original paper reports on much larger models. Whether that gap grows with model size is the question I'd test next.</p>

<h2>My poster</h2>
<object class="pdf" data="../assets/lora-dora-poster.pdf" type="application/pdf" aria-label="LoRA and DoRA project poster (PDF)">
  <p>Your browser can't show the poster here. <a href="../assets/lora-dora-poster.pdf">Open the poster PDF</a>.</p>
</object>

<p class="small muted">Full source, report and poster: <a href="https://github.com/arnavtevatia/lora-dora-gpt2">github.com/arnavtevatia/lora-dora-gpt2</a></p>
"""

# ---------------- GAN ----------------
GAN = """
<p class="crumb"><a href="index.html">Projects</a> / GAN loss demo</p>
<p class="eyebrow">Interactive explainer · HTML, CSS, JavaScript</p>
<h1>Why GANs use a different loss</h1>
<p class="lede">A GAN trains two networks against each other. The textbook loss gives the generator almost no signal early in training, exactly when it needs the most help. I built this demo so you can see and feel that problem, then see the fix.</p>

<div class="plain">
  <strong>In plain language</strong>
  Picture a student who gets almost no feedback while they are worst at a skill, and lots of feedback only once they are already good. The fix in this demo flips that, so the student gets the strongest feedback early on.
</div>

<div class="iframe-wrap">
  <iframe src="https://arnavtevatia.github.io/gan-loss-demo/" title="Interactive GAN loss curves demo" loading="lazy"></iframe>
</div>
<p class="small muted">Having trouble with the embedded view? <a href="https://arnavtevatia.github.io/gan-loss-demo/">Open the demo full screen</a>.</p>

<h2>What's mine and what isn't</h2>
<p>The non-saturating loss is not my idea. Goodfellow et al. proposed it in the original GAN paper (2014). What I made is this demo and its explanations: the design, the visuals, the simulation and the code.</p>

<h2>How it's built</h2>
<p>The demo walks through six steps: the two loss formulas side by side, live gradient meters that show the stall, proof that both losses end in the same place, a speed race where each bar moves at the speed of its gradient, a small training simulation, and a free exploration mode.</p>
"""

# ---------------- About ----------------
ABOUT = """
<p class="eyebrow">About</p>
<h1>Same loop, two settings</h1>
<p class="lede">I've captained Cornell's Division I men's squash team since my junior year. Squash and robotics reward the same habit: try something, look honestly at what happened, adjust, and repeat quickly.</p>

<div class="two">
  <div>
    <h2>On the court</h2>
    <p>I was named captain as a junior after our team graduated eight seniors, so a young roster had to rebuild its standards fast. As captain I coordinate training and recruitment for more than 15 athletes. Before Cornell, I won gold for Team USA at the 2022 Pan American Junior Games.</p>
  </div>
  <div>
    <h2>In the lab</h2>
    <p>On my projects I run controlled comparisons, read the measured results instead of the hoped-for ones, and change one thing at a time. My <a href="projects/cuda-kernels.html">GPU kernels</a> went through four versions that way, and my <a href="projects/lora-dora.html">LoRA project</a> found a result I didn't expect because I measured it.</p>
  </div>
</div>

<h2>The loop</h2>
<ol class="loop" aria-label="Four-stage loop: Try, Observe, Adjust, Repeat">
  <li><b>1. Try</b>
    <p class="side"><span>Squash</span>Run a drill with one specific intention.</p>
    <p class="side"><span>Robotics</span>Run an experiment with one clear question.</p></li>
  <li><b>2. Observe</b>
    <p class="side"><span>Squash</span>Watch where the ball lands and review the match.</p>
    <p class="side"><span>Robotics</span>Read the measured result and the failure logs.</p></li>
  <li><b>3. Adjust</b>
    <p class="side"><span>Squash</span>Change one thing in the next game plan.</p>
    <p class="side"><span>Robotics</span>Change one variable in the next version.</p></li>
  <li><b>4. Repeat</b>
    <p class="side"><span>Squash</span>Short loops, every practice.</p>
    <p class="side"><span>Robotics</span>Short loops, every build.</p></li>
</ol>

<h2>The team I'm looking for</h2>
<p>I work best with clear standards, direct feedback and short loops between trying something and seeing whether it worked. That's what a good squash team runs on, and it's what I want in an engineering team: small enough that everyone owns something real, and close enough to hardware that problems show up fast.</p>

<h2>Outside of engineering</h2>
<ul>
  <li>Community Outreach Chair, Men of Color in Athletics (MOCA)</li>
  <li>Member, Sigma Pi</li>
</ul>
"""

# ---------------- Contact ----------------
CONTACT = """
<p class="eyebrow">Resume &amp; Contact</p>
<h1>Let's talk</h1>
<p class="lede">I'm looking for a full-time software engineering role at a robotics or physical AI company, ideally lower in the stack. I can start as early as January 2027.</p>

<div class="grid">
  <a class="card" href="https://www.linkedin.com/in/arnav-tevatia">
    <h3>LinkedIn</h3>
    <p class="muted">The best way to reach me and see my full experience.</p>
    <span class="more">linkedin.com/in/arnav-tevatia →</span>
  </a>
  <a class="card" href="https://github.com/arnavtevatia">
    <h3>GitHub</h3>
    <p class="muted">Source code for every project on this site.</p>
    <span class="more">github.com/arnavtevatia →</span>
  </a>
</div>

<h2>Education</h2>
<p><strong>Cornell University, College of Engineering</strong>, Class of 2027<br>
B.S. Computer Science, machine learning concentration</p>
"""

page("index.html", "Home", "home", HOME, "Arnav Tevatia, Cornell CS senior building ML systems for robotics and physical AI.")
page("projects/index.html", "Projects", "projects", PROJECTS, "Engineering projects by Arnav Tevatia.")
page("projects/teleoperation.html", "Teleoperation force feedback", "projects", TELEOP, "Force feedback for robot teleoperation, robotics internship.")
page("projects/cuda-kernels.html", "GPU kernels", "projects", CUDA, "CUDA matrix multiply kernels for transformer inference.")
page("projects/lora-dora.html", "LoRA and DoRA", "projects", LORA, "LoRA and DoRA fine-tuning on GPT-2 from scratch.")
page("projects/gan-demo.html", "GAN loss demo", "projects", GAN, "Interactive explainer of the non-saturating GAN loss.")
page("about.html", "About", "about", ABOUT, "How squash captaincy and robotics engineering connect for Arnav Tevatia.")
page("contact.html", "Resume & Contact", "contact", CONTACT, "Contact Arnav Tevatia.")
print("built")
