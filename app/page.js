'use client';
import TiltedCard from './components/circular-gallery/app'
import Galaxy from './components/background/app'
import SplitText from './components/text/app'
import data from './data.json'
import Image from 'next/image';
import Link from 'next/link';
import dynamic from 'next/dynamic';

const colors = ['bg-red-400', 'bg-green-400', 'bg-blue-400', 'bg-purple-400, bg-yellow-400, bg-pink-400'];

export default function Home() {
  const SmoothScroll = dynamic(() => import('./components/SmoothScrollWrapper'), {
  ssr: false,
  });
    return (
      <div>
        <div className="inset-0 z-0 fixed" >
                <Galaxy />
              </div>
        <SmoothScroll>
          <div data-scroll-container>
            <div className="mt-5 flex flex-col w-full min-h-screen justify-center overflow-x-hidden items-center">
              <SplitText 
                  text="Web Kelas X SIJA 1"
                  tag="h1"
                  className="text-4xl md:text-6xl lg:text-8xl font-extrabold text-white"
                  textAlign="center"
                />
              <div className="mt-9 sm:w-[50%] grid lg:grid-cols-4 relative justify-between sm:grid sm:grid-cols-2 items-center lg:w-full">
                {data.map((item, i)=>(
                  <Link href={item.Link} key={i} className={`m-4 p-1 rounded-lg shadow-lg items-center`}>
                    <TiltedCard
                      imageSrc={item.image}
                      captionText={item.title}
                      containerHeight="250px"
                      containerWidth="200px"
                      imageHeight="250px"
                      imageWidth="200px"
                      rotateAmplitude={20}
                      scaleOnHover={1.2}
                      showMobileWarning={false}
                      showTooltip={true}
                      displayOverlayContent={true}
                      overlayContent={
                        <p className="bg-[#2626266d] rounded-[4px] px-[6px] py-[2px] text-sm font-semibold">
                          {item.title}
                        </p>
                      }
                    />
                  </Link>
                ))}
              </div>
          </div>
          </div>
      </SmoothScroll>
    </div>
    )
}