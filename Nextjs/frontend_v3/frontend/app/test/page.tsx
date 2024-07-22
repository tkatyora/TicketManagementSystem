import Image from 'next/image';
import EventInfo from '@/app/componets/eventInfo';
import React from 'react';

const HomePage = () => {
  return (
    <>
      <div className="carousel w-full">
        <div id="slide1" className="carousel-item relativ w-full">
          <Image
            src="/Images/code.jpg"
            alt="Slide 1"
            layout="fill"
            objectFit="cover"
            className="w-full"
          />
          <div className="absolute left-5 right-5 top-1/2 flex -translate-y-1/2 transform justify-between">
            <a href="#slide4" className="btn btn-circle">❮</a>
            <a href="#slide2" className="btn btn-circle">❯</a>
          </div>
        </div>
        <div id="slide2" className="carousel-item relative w-full">
          <Image
            src=""
            alt="Slide 2"
            layout="fill"
            objectFit="cover"
            className="w-full"
          />
          <div className="absolute left-5 right-5 top-1/2 flex -translate-y-1/2 transform justify-between">
            <a href="#slide1" className="btn btn-circle">❮</a>
            <a href="#slide3" className="btn btn-circle">❯</a>
          </div>
        </div>
        <div id="slide3" className="carousel-item relative w-full">
          <Image
            src=""
            alt="Slide 3"
            layout="fill"
            objectFit="cover"
            className="w-full"
          />
          <div className="absolute left-5 right-5 top-1/2 flex -translate-y-1/2 transform justify-between">
            <a href="#slide2" className="btn btn-circle">❮</a>
            <a href="#slide4" className="btn btn-circle">❯</a>
          </div>
        </div>
        <div id="slide4" className="carousel-item relative w-full">
          <Image
            src=""
            alt="Slide 4"
            layout="fill"
            objectFit="cover"
            className="w-full"
          />
          <div className="absolute left-5 right-5 top-1/2 flex -translate-y-1/2 transform justify-between">
            <a href="#slide3" className="btn btn-circle">❮</a>
            <a href="#slide1" className="btn btn-circle">❯</a>
          </div>
        </div>
      </div>
      <EventInfo />
    </>
  );
};

export default HomePage;
