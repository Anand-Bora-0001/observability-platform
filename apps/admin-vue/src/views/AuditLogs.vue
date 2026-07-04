<template>
  <div>
    <h1 class="text-2xl font-bold text-white mb-6">Security Audit Logs</h1>
    <div class="bg-gray-900 border border-gray-800 rounded-xl overflow-hidden p-6">
      <div class="space-y-4">
        <div v-for="log in logs" :key="log.id" class="border-b border-gray-800 pb-4">
          <div class="flex items-center space-x-2 text-sm">
            <span class="text-blue-400 font-mono">{{ log.timestamp }}</span>
            <span class="text-gray-300">{{ log.user }} performed</span>
            <span class="text-white font-semibold">{{ log.action }}</span>
            <span class="text-gray-500">from {{ log.ip }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const logs = ref([
  { id: 1, timestamp: '2026-07-04T18:00:00Z', user: 'alice@example.com', action: 'Update_User_Role', ip: '192.168.1.5' },
  { id: 2, timestamp: '2026-07-04T17:45:00Z', user: 'bob@example.com', action: 'Failed_Login_Attempt', ip: '10.0.0.99' },
  { id: 3, timestamp: '2026-07-04T16:30:00Z', user: 'system', action: 'Rotate_TLS_Cert', ip: 'internal' },
])
</script>
