<template>
  <div class="min-h-screen bg-gray-950 flex flex-col">
    <!-- Navbar -->
    <header class="bg-gray-900 border-b border-gray-800">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
        <div class="flex items-center space-x-3">
          <Shield class="text-blue-500 w-8 h-8" />
          <span class="text-xl font-bold text-white tracking-tight">Identity Admin</span>
        </div>
        <nav class="flex space-x-6">
          <router-link to="/" class="text-gray-300 hover:text-white transition-colors">Users</router-link>
          <router-link to="/groups" class="text-gray-300 hover:text-white transition-colors">Groups</router-link>
          <router-link to="/audit" class="text-gray-300 hover:text-white transition-colors">Audit Logs</router-link>
        </nav>
        <div class="flex items-center">
          <div class="w-8 h-8 bg-gray-800 rounded-full flex items-center justify-center border border-gray-700">
            <User class="text-gray-400 w-5 h-5" />
          </div>
        </div>
      </div>
    </header>

    <!-- Main Content -->
    <main class="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <router-view />
    </main>
  </div>
</template>

<script setup lang="ts">
import { Shield, User } from 'lucide-vue-next'
</script>
