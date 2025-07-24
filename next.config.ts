// // import type { NextConfig } from "next";

// // const nextConfig: NextConfig = {
// //   /* config options here */
// // };

// // export default nextConfig;




// import type { NextConfig } from "next";

// const nextConfig: NextConfig = {
//   images: {
//     remotePatterns: [
//       {
//         protocol: 'https',
//         hostname: 'www.kiminona.com',
//       },
//       {
//         protocol: 'https',
//         hostname: 'image.tmdb.org',
//       },
//       { // ↓↓↓ これを追加 ↓↓↓
//         protocol: 'http',
//         hostname: 'localhost',
//         port: '8000',
//       },
//     ],
//   },
// };

// export default nextConfig;


// frontend/next.config.ts

import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  images: {
    remotePatterns: [
      {
        protocol: 'http',
        hostname: 'localhost',
        port: '8000',
        pathname: '/media/',
      },
      // 他のドメインも必要に応じて追加できます
    ],
  },
};

export default nextConfig;