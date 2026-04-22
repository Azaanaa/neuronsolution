async function loadAppSettings() {
  try {
    const res = await fetch("/settings/");
    if (!res.ok) return;
    const list = await res.json();
    const map = {};
    list.forEach((s) => (map[s.setting_key] = s.setting_value));

    const appName = map.app_name || "Neuron Solution";
    const appSubtitle = map.app_subtitle || "";

    document.title = appName;

    document.querySelectorAll("[data-app-name]").forEach((el) => {
      el.textContent = appName;
    });
    document.querySelectorAll("[data-app-subtitle]").forEach((el) => {
      el.textContent = appSubtitle;
    });
    document.querySelectorAll("[data-app-header]").forEach((el) => {
      const suffix = el.getAttribute("data-app-header");
      el.textContent = appName + (suffix ? " — " + suffix : "");
    });
  } catch (e) {
    console.warn("Settings ачаалахад алдаа", e);
  }
}

loadAppSettings();

(function () {
  const container = document.createElement("div");
  container.innerHTML = `
    <div id="ns-modal-bg" style="display:none; position:fixed; inset:0; background:rgba(0,0,0,0.4); z-index:9999; align-items:center; justify-content:center;">
      <div style="background:white; border-radius:10px; padding:24px; width:340px; box-shadow:0 10px 40px rgba(0,0,0,0.15);">
        <div id="ns-modal-icon" style="width:44px; height:44px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:22px; font-weight:bold; margin:0 auto 14px;"></div>
        <h3 id="ns-modal-title" style="font-size:15px; color:#1a1a2e; text-align:center; margin-bottom:8px;"></h3>
        <p id="ns-modal-msg" style="font-size:13px; color:#666; text-align:center; margin-bottom:18px; line-height:1.5;"></p>
        <div style="display:flex; gap:8px;">
          <button id="ns-modal-cancel" style="flex:1; padding:9px; border:1px solid #ddd; border-radius:6px; background:#f5f5f5; cursor:pointer; font-size:13px;">Болих</button>
          <button id="ns-modal-ok" style="flex:1; padding:9px; border:none; border-radius:6px; background:#1a1a2e; color:white; cursor:pointer; font-size:13px; font-weight:600;">OK</button>
        </div>
      </div>
    </div>
  `;
  document.body.appendChild(container);

  const bg = document.getElementById("ns-modal-bg");
  const icon = document.getElementById("ns-modal-icon");
  const title = document.getElementById("ns-modal-title");
  const msg = document.getElementById("ns-modal-msg");
  const okBtn = document.getElementById("ns-modal-ok");
  const cancelBtn = document.getElementById("ns-modal-cancel");

  let currentResolve = null;

  function close(result) {
    bg.style.display = "none";
    if (currentResolve) {
      currentResolve(result);
      currentResolve = null;
    }
  }

  okBtn.onclick = () => close(true);
  cancelBtn.onclick = () => close(false);
  bg.onclick = (e) => {
    if (e.target === bg) close(false);
  };

  function show({ type, titleText, msgText, showCancel, okText }) {
    const styles = {
      success: { bg: "#d1fae5", color: "#065f46", mark: "✓" },
      error: { bg: "#fee2e2", color: "#991b1b", mark: "✕" },
      warn: { bg: "#fef3c7", color: "#92400e", mark: "!" },
      confirm: { bg: "#dbeafe", color: "#1e40af", mark: "?" },
      info: { bg: "#e0e7ff", color: "#3730a3", mark: "i" },
    };
    const s = styles[type] || styles.info;
    icon.style.background = s.bg;
    icon.style.color = s.color;
    icon.textContent = s.mark;
    title.textContent = titleText || "";
    msg.textContent = msgText || "";
    okBtn.textContent = okText || "OK";
    cancelBtn.style.display = showCancel ? "" : "none";
    bg.style.display = "flex";

    return new Promise((resolve) => {
      currentResolve = resolve;
    });
  }

  window.nsAlert = (msgText, titleText = "Мэдэгдэл") =>
    show({ type: "info", titleText, msgText, showCancel: false });

  window.nsSuccess = (msgText, titleText = "Амжилттай") =>
    show({ type: "success", titleText, msgText, showCancel: false });

  window.nsError = (msgText, titleText = "Алдаа гарлаа") =>
    show({ type: "error", titleText, msgText, showCancel: false });

  window.nsWarn = (msgText, titleText = "Анхаарна уу") =>
    show({ type: "warn", titleText, msgText, showCancel: false });

  window.nsConfirm = (msgText, titleText = "Баталгаажуулах", okText = "Тийм") =>
    show({ type: "confirm", titleText, msgText, showCancel: true, okText });
})();
