document
  .getElementById("pagoForm")
  .addEventListener("submit", async (event) => {
    event.preventDefault();

    const monto = document.getElementById("monto").value;
    const subject = document.getElementById("subject").value;
    const correo = document.getElementById("correo").value;

    try {
      const response = await fetch("/crear_pago", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ monto, subject, correo }),
      });

      const data = await response.json();

      if (!data.payment_id) {
        throw new Error("No se recibió payment_id");
      }

      window.location.href = `/estado_pago?payment_id=${data.payment_id}`;
    } catch (err) {
      console.error("Error al iniciar el pago:", err);
      alert("Hubo un problema al iniciar el pago.");
    }
  });
