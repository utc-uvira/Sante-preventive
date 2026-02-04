<!doctype html>
<html lang="fr">
<head>  
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Mélanges naturels – Santé préventive</title>

  <!-- Primary meta -->
  <meta name="description" content="Plateforme civique de recommandations de mélanges naturels (infusions, smoothies, jus) par objectifs santé. Information éducative, non médicale." />

  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website" />
  <meta property="og:title" content="Mélanges naturels – Santé préventive" />
  <meta property="og:description" content="Choisissez un objectif santé (digestion, immunité, énergie, sommeil, etc.) et obtenez 2–3 mélanges recommandés. Information éducative, non médicale." />
  <meta property="og:image" content="./og-image.png" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta property="og:locale" content="fr_FR" />

  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="Mélanges naturels – Santé préventive" />
  <meta name="twitter:description" content="Recommandations de mélanges naturels par objectifs santé (MVP). Information éducative, non médicale." />
  <meta name="twitter:image" content="./og-image.png" />

  <style>
    :root { color-scheme: light; }
    body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; margin: 0; background: #f5f7fa; color: #111827; }
    .wrap { max-width: 900px; margin: 0 auto; padding: 28px 18px 48px; }
    .card { background: white; border: 1px solid #d1d5db; border-radius: 16px; padding: 22px; box-shadow: 0 1px 0 rgba(0,0,0,.02); }
    h1 { margin: 0 0 8px; font-size: 28px; }
    p { margin: 10px 0; line-height: 1.45; }
    .badge { display: inline-block; padding: 6px 10px; border-radius: 999px; background: #e8f8ef; border: 1px solid #bbf7d0; font-weight: 600; font-size: 13px; }
    .row { display: grid; grid-template-columns: 1fr; gap: 14px; }
    @media (min-width: 860px) { .row { grid-template-columns: 1.2fr .8fr; align-items: start; } }
    .btn { display: inline-block; padding: 10px 14px; border-radius: 12px; border: 1px solid #111827; text-decoration: none; color: #111827; font-weight: 700; }
    .btn.primary { background: #22c55e; border-color: #22c55e; color: white; }
    .muted { color: #6b7280; font-size: 13px; }
    code { background: #f3f4f6; padding: 2px 6px; border-radius: 8px; }
    img { max-width: 100%; border-radius: 14px; border: 1px solid #e5e7eb; }
  </style>
</head>
<body>
  <div class="wrap">
    <div class="row">
      <div class="card">
        <span class="badge">MVP • éducatif</span>
        <h1>Mélanges naturels – Santé préventive</h1>
        <p id="lead">
          Sélectionnez un objectif santé (digestion, immunité, énergie, sommeil…) et obtenez 2–3 mélanges recommandés
          (ingrédients, bénéfices, précautions) avec un lien partageable.
        </p>
        <p class="muted">
          ⚠️ Cette plateforme fournit une information <strong>éducative</strong> et <strong>préventive</strong> uniquement.
          Elle ne remplace pas un avis médical.
        </p>

        <p>
          <a id="openApp" class="btn primary" href="#">Ouvrir l’application</a>
          <a class="btn" href="#" onclick="copyLink(); return false;">Copier le lien</a>
        </p>

        <p class="muted">
          Astuce : partagez une URL comme <code>?goal=DIGESTION</code> ou <code>?goal=SOMMEIL&mix=infusion-feuilles-de-corossol-gingembre</code>.
        </p>
      </div>

      <div class="card">
        <img src="./og-image.png" alt="Aperçu partage" />
        <p class="muted" style="margin-top:10px">
          Cette page sert d’aperçu (Open Graph) pour WhatsApp/Facebook/X/LinkedIn.
        </p>
      </div>
    </div>
  </div>

<script>
  function getQuery() {
    const params = new URLSearchParams(window.location.search);
    return {
      goal: params.get("goal") || "",
      mix: params.get("mix") || ""
    };
  }

  // TODO: Remplacez APP_URL par l’URL publique de votre Streamlit (une fois déployé)
  const APP_URL = "https://YOUR-STREAMLIT-APP-URL";

  const q = getQuery();
  const qs = new URLSearchParams();
  if (q.goal) qs.set("goal", q.goal);
  if (q.mix) qs.set("mix", q.mix);

  const appLink = APP_URL + (qs.toString() ? ("?" + qs.toString()) : "");
  document.getElementById("openApp").href = appLink;

  // Personalize lead text if params exist
  if (q.goal || q.mix) {
    const parts = [];
    if (q.goal) parts.push("objectif: " + q.goal);
    if (q.mix) parts.push("mélange: " + q.mix);
    document.getElementById("lead").textContent =
      "Lien de recommandation (" + parts.join(", ") + "). Ouvrez l’application pour voir les détails.";
  }

  async function copyLink() {
    try {
      await navigator.clipboard.writeText(window.location.href);
      alert("Lien copié !");
    } catch (e) {
      prompt("Copiez ce lien :", window.location.href);
    }
  }
</script>
</body>
</html>
