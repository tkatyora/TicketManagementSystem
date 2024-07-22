"use client";
import React, { useEffect } from 'react';

const EventInfo = () => {
  useEffect(() => {
    const textToType = "Winky D at HICC @22/04/2024";
    let index = 0;
    let isDeleting = false;
    const speed = 100;

    function typeText() {
      let currentText = textToType.substring(0, index);

      if (isDeleting) {
        index--;
        if (index < 0) {
          index = 0;
          isDeleting = false;
        }
      } else {
        index++;
        if (index > textToType.length) {
          index = textToType.length;
          isDeleting = true;
        }
      }

      document.getElementById("typedText").innerHTML = currentText;

      const delta = isDeleting ? speed / 2 : speed;
      setTimeout(typeText, delta);
    }

    typeText();

    // Countdown timer
    const endDate = new Date("2024-04-22T00:00:00");
    const countdownElement = document.getElementById("ticketsCount");
    const clockIcon = document.querySelector("#ticketsRemaining .fa-clock");

    function updateCountdown() {
      const now = new Date();
      const timeRemaining = endDate - now;

      if (timeRemaining <= 0) {
        clearInterval(countdownInterval);
        countdownElement.textContent = "0";
        clockIcon.classList.remove("fa-spin");
        document.getElementById("ticketsRemaining").textContent = "Sorry, tickets are sold out!";
      } else {
        const daysRemaining = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
        countdownElement.textContent = daysRemaining;
        clockIcon.classList.add("fa-spin");
      }
    }

    // Update countdown every second
    const countdownInterval = setInterval(updateCountdown, 1000);

    // Clean up interval on component unmount
    return () => clearInterval(countdownInterval);
  }, []);

  return (
    <div className="container mx-auto my-5">
      <div className="bg-gray-100 p-5 rounded">
        <div className="sm:w-8/12 py-5 mx-auto">
          <h1 className="text-5xl font-normal">
            <span id="typedText"></span>
          </h1>
          <p className="text-lg">
            Don&apos;t miss out on an electrifying performance by Winky D at the HICC on April 22, 2024.
            Experience a night filled with pulsating beats, soulful melodies, and unforgettable moments.
            Secure your tickets now to be part of this extraordinary event!
          </p>
          <span id="ticketsRemaining" className="text-center block mt-3">
            <i className="fas fa-clock text-4xl text-blue-500"></i> Hurry up! Only <span id="ticketsCount">2</span> tickets left!
          </span>
        </div>
      </div>
    </div>
  );
};

export default EventInfo;
