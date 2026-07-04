<template>
  <div>
    <div class="flex justify-between items-center mb-6">
      <div>
        <h1 class="text-2xl font-bold text-white">User Management</h1>
        <p class="text-gray-400 text-sm mt-1">Manage corporate identities, roles, and MFA status.</p>
      </div>
      <button class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg font-medium transition-colors">
        Provision User
      </button>
    </div>

    <div class="bg-gray-900 border border-gray-800 rounded-xl overflow-hidden">
      <table class="w-full text-left">
        <thead class="bg-gray-800/50 text-gray-400 text-sm">
          <tr>
            <th class="px-6 py-4 font-medium">Identity</th>
            <th class="px-6 py-4 font-medium">Organization</th>
            <th class="px-6 py-4 font-medium">Role</th>
            <th class="px-6 py-4 font-medium">MFA Status</th>
            <th class="px-6 py-4 font-medium">Status</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-800 text-sm">
          <tr v-for="user in users" :key="user.id" class="hover:bg-gray-800/50">
            <td class="px-6 py-4">
              <div class="font-medium text-white">{{ user.name }}</div>
              <div class="text-gray-400">{{ user.email }}</div>
            </td>
            <td class="px-6 py-4 text-gray-300">{{ user.org }}</td>
            <td class="px-6 py-4 text-gray-300">
              <span class="px-2 py-1 bg-gray-800 rounded-md text-xs border border-gray-700">{{ user.role }}</span>
            </td>
            <td class="px-6 py-4">
              <span :class="user.mfa ? 'text-green-400' : 'text-red-400'">{{ user.mfa ? 'Enrolled' : 'Not Enrolled' }}</span>
            </td>
            <td class="px-6 py-4">
              <span class="w-2 h-2 rounded-full inline-block mr-2" :class="user.active ? 'bg-green-500' : 'bg-red-500'"></span>
              <span class="text-gray-300">{{ user.active ? 'Active' : 'Suspended' }}</span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const users = ref([
  { id: 1, name: 'Alice SRE', email: 'alice@example.com', org: 'Engineering', role: 'Super Admin', mfa: true, active: true },
  { id: 2, name: 'Bob Developer', email: 'bob@example.com', org: 'Product', role: 'Viewer', mfa: false, active: true },
  { id: 3, name: 'Eve Terminated', email: 'eve@example.com', org: 'Sales', role: 'Editor', mfa: true, active: false },
])
</script>
