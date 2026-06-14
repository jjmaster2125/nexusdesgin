import webview

html = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Landed</title>

<style>
*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:'Segoe UI',sans-serif;
}

body{
    height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    overflow:hidden;
    background:#0f172a;
}

/* Animated Background */
.bg{
    position:fixed;
    inset:0;
    background:linear-gradient(
        -45deg,
        #0f172a,
        #1e293b,
        #3b82f6,
        #7c3aed
    );
    background-size:400% 400%;
    animation:gradientMove 12s ease infinite;
}

@keyframes gradientMove{
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
}

/* Glass Card */
.card{
    position:relative;
    z-index:10;

    width:500px;
    max-width:90%;

    padding:50px;

    background:rgba(255,255,255,0.08);

    border:1px solid rgba(255,255,255,0.15);

    backdrop-filter:blur(20px);

    border-radius:25px;

    text-align:center;

    box-shadow:
        0 8px 32px rgba(0,0,0,0.35);

    animation:fadeUp 1.2s ease;
}

@keyframes fadeUp{
    from{
        opacity:0;
        transform:translateY(40px);
    }

    to{
        opacity:1;
        transform:translateY(0);
    }
}

h1{
    color:white;
    font-size:3rem;
    font-weight:700;
    margin-bottom:15px;
}

p{
    color:rgba(255,255,255,0.75);
    font-size:1.1rem;
    line-height:1.6;
}

/* Glow Circle */
.glow{
    position:absolute;
    width:300px;
    height:300px;

    background:#3b82f6;
    filter:blur(150px);

    opacity:.35;

    border-radius:50%;

    top:-100px;
    right:-100px;
}

.glow2{
    position:absolute;
    width:250px;
    height:250px;

    background:#7c3aed;
    filter:blur(150px);

    opacity:.30;

    border-radius:50%;

    bottom:-100px;
    left:-100px;
}
</style>
</head>

<body>

<div class="bg"></div>

<div class="glow"></div>
<div class="glow2"></div>

<div class="card">
    <h1>🚀 You Have Landed</h1>
    <p>
        Welcome aboard.<br>
        Everything loaded successfully.
    </p>
</div>

</body>
</html>
"""

window = webview.create_window(
    "Landing Page",
    html=html,
    width=1000,
    height=650,
    resizable=True
)

webview.start()
