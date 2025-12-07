/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',     // <-- enables static export
  trailingSlash: true,  // optional, ensures URLs end with '/'
}

export default nextConfig;