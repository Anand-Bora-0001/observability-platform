import React from 'react';
import { NavLink } from 'react-router-dom';
import { LayoutDashboard, Server, AlertTriangle, Settings, Activity, Ticket as TicketIcon } from 'lucide-react';

const Sidebar: React.FC = () => {
  const navItems = [
    { to: '/dashboard', icon: <LayoutDashboard size={20} />, label: 'Dashboard' },
    { to: '/servers', icon: <Server size={20} />, label: 'Servers' },
    { to: '/incidents', icon: <AlertTriangle size={20} />, label: 'Incidents' },
    { to: '/tickets', icon: <TicketIcon size={20} />, label: 'Tickets' },
    { to: '/settings', icon: <Settings size={20} />, label: 'Settings' },
  ];

  return (
    <div className="flex flex-col w-64 bg-gray-900 border-r border-gray-800 text-gray-300">
      <div className="flex items-center justify-center h-20 border-b border-gray-800">
        <div className="flex items-center space-x-2 text-white font-bold text-xl">
          <div className="p-2 bg-blue-500 rounded-lg">
            <Activity size={24} />
          </div>
          <span>Observability</span>
        </div>
      </div>
      <div className="flex flex-col flex-1 overflow-y-auto mt-6">
        <nav className="flex-1 px-4 space-y-2 bg-gray-900">
          {navItems.map((item) => (
            <NavLink
              key={item.to}
              to={item.to}
              className={({ isActive }) =>
                `flex items-center px-4 py-3 text-sm font-medium rounded-lg transition-colors ${
                  isActive
                    ? 'bg-gray-800 text-blue-400'
                    : 'text-gray-400 hover:bg-gray-800 hover:text-white'
                }`
              }
            >
              {item.icon}
              <span className="ml-3">{item.label}</span>
            </NavLink>
          ))}
        </nav>
      </div>
    </div>
  );
};

export default Sidebar;
