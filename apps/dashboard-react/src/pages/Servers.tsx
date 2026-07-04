import React from 'react';
import { Server, Activity, Power, PowerOff } from 'lucide-react';

const mockServers = [
  { id: 1, hostname: 'web-prod-01', ip: '10.0.0.10', os: 'Linux', status: 'active', cpu: '45%', memory: '60%' },
  { id: 2, hostname: 'db-prod-01', ip: '10.0.0.11', os: 'Linux', status: 'active', cpu: '85%', memory: '90%' },
  { id: 3, hostname: 'cache-01', ip: '10.0.0.12', os: 'Linux', status: 'active', cpu: '15%', memory: '30%' },
  { id: 4, hostname: 'win-util-01', ip: '10.0.0.20', os: 'Windows', status: 'maintenance', cpu: '-', memory: '-' },
  { id: 5, hostname: 'web-prod-02', ip: '10.0.0.13', os: 'Linux', status: 'inactive', cpu: '-', memory: '-' },
];

const Servers: React.FC = () => {
  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-2xl font-bold text-white">Servers</h1>
          <p className="text-gray-400">Manage and monitor infrastructure assets</p>
        </div>
        <button className="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg shadow-sm transition-colors flex items-center space-x-2">
          <Server size={18} />
          <span>Add Server</span>
        </button>
      </div>

      <div className="bg-gray-900 border border-gray-800 rounded-xl overflow-hidden">
        <table className="min-w-full divide-y divide-gray-800">
          <thead className="bg-gray-800/50">
            <tr>
              <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase tracking-wider">Hostname</th>
              <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase tracking-wider">IP Address</th>
              <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase tracking-wider">OS</th>
              <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase tracking-wider">Status</th>
              <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase tracking-wider">Resource Usage</th>
              <th scope="col" className="px-6 py-3 text-right text-xs font-medium text-gray-400 uppercase tracking-wider">Actions</th>
            </tr>
          </thead>
          <tbody className="bg-gray-900 divide-y divide-gray-800 text-sm">
            {mockServers.map((server) => (
              <tr key={server.id} className="hover:bg-gray-800/50 transition-colors">
                <td className="px-6 py-4 whitespace-nowrap font-medium text-white flex items-center space-x-3">
                  <Server size={18} className="text-gray-400" />
                  <span>{server.hostname}</span>
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-gray-300">{server.ip}</td>
                <td className="px-6 py-4 whitespace-nowrap text-gray-400">{server.os}</td>
                <td className="px-6 py-4 whitespace-nowrap">
                  <span className={`px-2.5 py-1 inline-flex text-xs leading-5 font-semibold rounded-full 
                    ${server.status === 'active' ? 'bg-green-900/50 text-green-400' : 
                      server.status === 'maintenance' ? 'bg-yellow-900/50 text-yellow-400' : 
                      'bg-red-900/50 text-red-400'}`}>
                    {server.status.charAt(0).toUpperCase() + server.status.slice(1)}
                  </span>
                </td>
                <td className="px-6 py-4 whitespace-nowrap">
                  {server.status === 'active' ? (
                    <div className="flex items-center space-x-4 text-xs text-gray-400">
                      <span className="flex items-center"><Activity size={14} className="mr-1 text-blue-400"/> CPU: {server.cpu}</span>
                      <span className="flex items-center"><Activity size={14} className="mr-1 text-purple-400"/> RAM: {server.memory}</span>
                    </div>
                  ) : (
                    <span className="text-gray-500">N/A</span>
                  )}
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                  <button className="text-gray-400 hover:text-white transition-colors">
                    {server.status === 'active' ? <PowerOff size={18} className="hover:text-red-400"/> : <Power size={18} className="hover:text-green-400"/>}
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Servers;
