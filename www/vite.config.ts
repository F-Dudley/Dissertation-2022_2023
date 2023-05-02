import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'
import tsconfigPaths from 'vite-tsconfig-paths'
import Pages from 'vite-plugin-pages'

// https://vitejs.dev/config/
export default defineConfig({
  server: {
    port: 3000,
  },
  plugins: [
    react(),
    tsconfigPaths(),
    Pages({
      extensions: ['tsx', 'jsx']
    })
  ],
})
