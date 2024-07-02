import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    host: true, // This makes Vite listen on all network interfaces
    port: 5173, // Port on which Vite server will run
  },
});
